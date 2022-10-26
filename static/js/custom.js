const darkMode = document.querySelector(".theme-toggle");

function darkify() {
    if(sessionStorage.getItem('toggle')){
        document.documentElement.classList.toggle(sessionStorage.getItem('toggle'))
        sessionStorage.removeItem('toggle')
    } else {
        sessionStorage.setItem('toggle', 'theme--night')
        document.documentElement.classList.toggle(sessionStorage.getItem('toggle'))
    }
}

darkMode.addEventListener("click", darkify);

const check = () => {
    if(sessionStorage.getItem('toggle')){
        document.documentElement.classList.toggle(sessionStorage.getItem('toggle'))
    }
}

check()