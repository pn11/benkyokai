using Images, ImageView

function main()
    img = Gray.(load("cat.png"))
    template = Gray.(load("template.png"))
    imshow(img)
    println(typeof(img))
    rows, cols = size(img)

    if check_size(img, template)
        match_template(img, template, "SSD")
    end

end

function check_size(img, template)
    r_img, c_img = size(img)
    r_tmp, c_tmp = size(template)
    if r_tmp > r_img || c_tmp > c_img
        return false
    end
    return true
end


function ssd(img, template)
    r_img, c_img = size(img)
    r_tmp, c_tmp = size(template)
    ssd_map = zeros((r_img - r_tmp + 1, c_img - c_tmp + 1))
    for y in 1:r_img - r_tmp + 1
        for x in 1:c_img - c_tmp + 1
            ssd_value = 0
            for yt in 1:c_tmp
                for xt in 1:r_tmp
                    ssd_value += (img[y+yt-1, x+xt-1] - template[yt, xt])^2
                end
            end
            ssd_map[y, x] = ssd_value
        end
    end
    return ssd_map
end


function match_template(img, template, mode)
    println("Template matching")
    ssd_img = ssd(img, template)
    imshow(ssd_img)
end

main()
