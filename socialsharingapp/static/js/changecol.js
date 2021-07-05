let cheknight = document.getElementById('flexSwitchCheckDefault');
cheknight.addEventListener('click', function () {
    let whitebox = document.getElementsByClassName('mainCard');
    let wkowwmLogo = document.getElementsByClassName('wkowwmLogo');
    let profileTitle = document.getElementsByClassName('profileTitle');
    if (cheknight.checked == true) {
        document.body.style.backgroundColor = "#212529";
        for (let i = 0; i < whitebox.length; i++) {
            whitebox[i].style.backgroundColor = "#121212";
        }
        for (let i = 0; i < wkowwmLogo.length; i++) {
            wkowwmLogo[i].style.backgroundColor = "#212529";
        }
        for (let i = 0; i < profileTitle.length; i++) {
            profileTitle[i].style.color = "#f2f2f2";
        }
    } else {
        document.body.style.backgroundColor = "#f3f2f2";
        for (let i = 0; i < whitebox.length; i++) {
            whitebox[i].style.backgroundColor = "#FFF";
        }
        for (let i = 0; i < wkowwmLogo.length; i++) {
            wkowwmLogo[i].style.backgroundColor = "#f3f2f2";
        }
        for (let i = 0; i < profileTitle.length; i++) {
            profileTitle[i].style.color = "#000";
        }
    }
})

// https://uxdesign.cc/dark-mode-ui-design-the-definitive-guide-part-1-color-53dcfaea5129