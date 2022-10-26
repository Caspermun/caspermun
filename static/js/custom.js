const darkMode = document.querySelector(".theme-toggle");

function darkify() {
    if(localStorage.getItem('toggle')){
        document.documentElement.classList.toggle(localStorage.getItem('toggle'))
        localStorage.removeItem('toggle')
    } else {
        localStorage.setItem('toggle', 'theme--night')
        document.documentElement.classList.toggle(localStorage.getItem('toggle'))
    }
}

darkMode.addEventListener("click", darkify);

const check = () => {
    if(localStorage.getItem('toggle')){
        document.documentElement.classList.toggle(localStorage.getItem('toggle'))
    }
}

check()