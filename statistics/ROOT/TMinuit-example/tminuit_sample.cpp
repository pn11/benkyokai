#include<iostream>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<iomanip>
#include<memory>

#include<TROOT.h>
#include<TStyle.h>
#include<TFile.h>
#include<TTree.h>
#include<TCanvas.h>
#include<TH1.h>
#include<TH2.h>
#include<TF1.h>
#include<TLatex.h>
#include<TChain.h>
#include<TGraphErrors.h>
#include<TLine.h>
#include<TFitter.h>
#include<TVirtualFitter.h>

#include<TRandom.h>
#include<TMinuit.h>

/** ガウシアンの個数 */
const int num_gaus = 3; 

/**
 * @brief ガウシアンからヒストグラムを作る。
 */
TH1D* create_data_hist();

// グローバルスコープなので、これらはスマートポインタにすると
// インタプリタを終了したときにメモリリークする。
TF1 *fit_normal;
TF1 *fit_minuit;
TH1 *h_minuit;

double *par;
double *parErr;


/**
 * @brief aの絶対値が1.0e-5以下だったらゼロとみなす。
 */
bool is_zero(double a){
    return fabs(a) < 1.0e-5;
}

/**
 * @brief TMinuit で最小化するための関数。
 * @details パラメータの個数はガウシアンの数x3 (constant、mean, sigma)
 * 3*i個目がconstant、3*i+1個目がmean、3*i+2個目がsigma
 */
void min_func(Int_t &npar, Double_t *gin, Double_t &f, Double_t *par, Int_t iflag){
    double chi2 = 0;    
    const int nbins = h_minuit->GetNbinsX();

    for (int i = 0; i < npar; ++i){
        fit_minuit->SetParameter(i, par[i]);
        // std::cout << pastd::coutr[i] << std::endl;
    }
    
    
    // bin ID = 1 は underflow, bin ID = nbins+1 は overflow
    for (int i = 1; i < nbins+1; ++i){
        double bin_low = h_minuit->GetBinLowEdge(i);
        double bin_high = h_minuit->GetBinLowEdge(i+1);        
        double bin_value = h_minuit->GetBinContent(i); // observed value
        double bin_error = h_minuit->GetBinError(i);

        if (is_zero(bin_value)){
            continue;
        }

        double expected = fit_minuit->Integral(bin_low, bin_high) / (bin_high-bin_low); // bin_lowからbin_high まで積分して平均
        double diff = bin_value - expected; // observed と expected の差


        // エラーがゼロだと inf になるので適当な大きい値を入れる。
        // 正しい取扱い方は
        if (bin_error > 0){
            chi2 += diff*diff / (bin_error*bin_error);
        }
        else{
            chi2 += 1e8;
        }

        // std::cout << bin_low << "-" << bin_high << " : " << bin_value << ", " << bin_error << std::endl;
        // std::cout << "Chi2 = " << chi2 << std::endl;
    }

    f = chi2;
}


/**
 * @brief メイン関数
 * 
 */
#ifdef __CINT__
int tminuit_sample(){
#else
int main(){
#endif
    auto c = std::unique_ptr<TCanvas>(new TCanvas("c", "c"));
    c->Divide(1, 2);

    std::string func_str = "gaus(0)";
    for (int i = 1; i < num_gaus; ++i){
        func_str += std::string(Form("+gaus(%d)", 3*i));
    }

    fit_normal = new TF1("fit_normal", func_str.c_str(), 0, 4000) ;
    fit_minuit = new TF1("fit_minuit", func_str.c_str(), 0, 4000);

    const int npar = num_gaus * 3;

    par = new double[npar];
    parErr = new double[npar];

    std::unique_ptr<TMinuit> min(new TMinuit(npar));

    const double stepSize = 0.1;
    const double minVal = 0;
    const double maxVal = 10000;
    

    // 平均とシグマの初期値は既知とする。高さは全部とりあえず500。
    for (int i = 0; i < num_gaus; ++i){
        double mean = 1000*(i+1);
        double sigma = 500 / (i+1);

        // TH1::Fit 用の初期パラメータ設定
        fit_normal->SetParameter(3*i, 500);
        fit_normal->SetParameter(3*i+1, mean);
        fit_normal->SetParameter(3*i+2, sigma);

        // TMinuit 用の初期パラメータ設定
        par[3*i] = 500;
        par[3*i+1] = mean;
        par[3*i+2] = sigma;

        min->DefineParameter(3*i, Form("Constant %d", i), par[3*i], stepSize, minVal, maxVal);
        min->DefineParameter(3*i+1, Form("Mean %d", i), par[3*i+1], stepSize, minVal, maxVal);
        min->DefineParameter(3*i+2, Form("Sigma %d", i), par[3*i+2], stepSize, minVal, maxVal);
    }

    auto h = std::unique_ptr<TH1D>(create_data_hist());
    h_minuit = (TH1D*)h->Clone("h_minuit");
    h_minuit->SetTitle("fit by TMinuit");    
    auto h_normal = std::unique_ptr<TH1D>((TH1D*)h->Clone("h_normal"));
    h_normal->SetTitle("fit by TH1D::Fit()");

    min->SetFCN(min_func);
    min->Migrad();

    for (int i = 0; i < npar; i++){
        min->GetParameter(i, par[i], parErr[i]);
        fit_minuit->FixParameter(i, par[i]);
        std::cout << "Result: " << par[i] << " +/- " << parErr[i] << std::endl;
    }


    c->cd(1);
    h_minuit->Draw();
    fit_minuit->Draw("same");
    c->cd(2);
    h_normal->Fit(fit_normal, "IM"); // Iオプションはビン範囲での積分を行う。Mオプションは more
    c->Print("tminuit_sample.pdf", "pdf portrait");

    delete[] par;
    return 0;
}

TH1D* create_data_hist(){
    /** ガウシアン1個あたりのイベント数 */
    const int num_event = 100000;

    auto means = std::unique_ptr<double[]>(new double[num_gaus]);
    auto sigmas = std::unique_ptr<double[]>(new double[num_gaus]);

    for (int i = 0; i < num_gaus; ++i){
        means[i] = 1000*(i+1);
        sigmas[i] = 500 / (i+1);
    }

    std::unique_ptr<TRandom> rnd(new TRandom(65539));

    TH1D *h = new TH1D("h", "hist", 1000, 0, 4000);
    h->Sumw2();

    for (int j = 0; j < num_event; ++j){
        for (int i = 0; i < num_gaus; ++i){
            h->Fill(rnd->Gaus(means[i], sigmas[i]));
        }
    }

    return h;
}
