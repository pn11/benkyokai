if (Test-Path venv){
    venv/Scripts/activate.ps1
}
else{
    Write-Output "venv not found. Starting to create new one."
    python -m venv -r venv
    venv/Scripts/Activate.ps1
    pip install -r requirements.txt
}
