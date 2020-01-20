import Axios from "axios"

let navbar_item_user = document.querySelector('#navbar_item_user')
let form_login = document.querySelector('#form_login')
let form_testimoni = document.querySelector('#form_testimoni')
let form_register = document.querySelector('#form_register')
let form_blog = document.querySelector('#form_blog')
let title_blocks_cover = document.querySelector('#title_blocks_cover')
let title2_blocks_cover = document.querySelector('#title2_blocks_cover')
let button_user = document.getElementById('button_user')
let url = new URL(window.location.href)

let is_authenticated = (bol) => {
    if (bol) {
        form_testimoni.style.display = 'block'
        form_login.style.display = 'none'
        form_register.style.display = 'none'
    } else {
        form_testimoni.style.display = 'none'
        form_login.style.display = 'none'
        form_register.style.display = 'block'
    }
}

let modal_blog = (show) => {
    if (show) {
        document.querySelector('.blog').style.display = 'block'
        document.querySelector('.blog').style.zIndex = '2001'
        document.querySelector('.blog').style.opacity = '1'
    } else {
        document.querySelector('.blog').style.zIndex = '-2000'
        document.querySelector('.blog').style.opacity = '0'
        document.querySelector('.blog').style.display = 'none'
    }
}

let targetScroll = document.querySelector('.site-blocks-cover').offsetHeight + 
document.querySelector('.site-navbar').offsetHeight

document.querySelector('#form_login .login_btn_register').addEventListener('click', () => {
    form_register.reset()
    form_login.style.display = 'none'
    form_register.style.display = 'block'

    window.scrollTo({top: targetScroll, behavior: 'smooth'})
})

document.querySelector('#form_register .register_btn_login').addEventListener('click', () => {
    form_login.reset()
    form_login.style.display = 'block'
    form_register.style.display = 'none'
    
    window.scrollTo({top: targetScroll, behavior: 'smooth'})
})

form_login.addEventListener('submit', (event) => {
    event.preventDefault()
    let data = new FormData(form_login)
    Axios.post('/api/user/login', data)
    .then((response) => {
        console.log(response['data'])
        if (response['data']['success'] == 'true') {
            order_user = response['data']['order_user']

            document.querySelector('#form_testimoni #id_user').value = order_user
            console.log(document.querySelector('#form_testimoni #id_user').value)
            window.scrollTo({top: 0, behavior: 'smooth'})
            authenticated = true
            is_authenticated(authenticated)
            form_login.reset()
            title_blocks_cover.innerHTML = 'Enjoy Your Trip'
            title2_blocks_cover.innerHTML = `${response['data']['user']}`
            navbar_item_user.innerHTML = `Hi ${response['data']['user']}!`
            userModal(
                'Successful Login',
                'Enjoy your trip with our service.',
                true
            )
            button_user.innerHTML = 'Write Your Blog'
            button_user.removeAttribute('href')
        } else {
            userModal(
                'Failed Login',
                'Username or Password incorect.',
                true
            )
        }
    })
    .catch((error) => {
        console.log(error)
    })
})

form_register.addEventListener('submit', (event) => {
    event.preventDefault()
    let data = new FormData(form_register)
    Axios.post('/api/user/register', data)
    .then((response) => {
        console.log(response['data'])
        if (response['data']['success'] == 'true') {
            userModal(
                'Register Successful', 
                'Thanks for registration, check your email for activation account', 
                true
            )
        }
    })
    .catch((error) => {
        console.log(error)
    })
})

form_testimoni.addEventListener('submit', (event) => {
    event.preventDefault()
    let data = new FormData(form_testimoni)
    Axios.post('/api/user/testimoni', data)
    .then((response) => {
        console.log(response['data'])
        if (response['data']['success'] == 'true') {
            form_testimoni.reset()
            userModal(
                'Thanks For Your Testimoni',
                'Keep using ZeeTrav for your travel trips',
                true
            )
        }
    })
    .catch((error) => {
        console.log(error)
    })
})

form_blog.addEventListener('submit', (event) => {
    event.preventDefault()
    let data = new FormData(form_blog)
    Axios.post('/api/blog/write', data)
    .then((response) => {
        console.log(response['data'])
        if (response['data']['success'] == 'true') {
            form_blog.reset()
            modal_blog(false)
            userModal(
                'Thank You for Writing Here',
                'Keep writing here to share your experience.',
                true
            )
        }
    })
    .catch((error) => {

    })
})

document.querySelector('#form_blog #button_cancel_blog').addEventListener('click', () => {
    blank(false)
    modal_blog(false)
})

button_user.addEventListener('click', () => {
    if (authenticated) {
        blank(true)
        modal_blog(true)
    }
})

document.querySelector('#buttonLogout').addEventListener('click', (event) => {
    event.preventDefault()
    let data = {}
    Axios.post('/api/user/logout', data)
    .then((response) => {
        console.log(response['data'])
        if (response['data']['success'] == 'true') {
            form_blog.reset()
            form_login.reset()
            form_register.reset()
            form_testimoni.reset()
            navbar_item_user.innerHTML = `Register Now!`
            title_blocks_cover.innerHTML = 'Register Your Self'
            title2_blocks_cover.innerHTML = 'Register / Login'
            window.scrollTo({top: 0, behavior: 'smooth'})
            authenticated = false
            is_authenticated(authenticated)
            button_user.innerHTML = 'About ZeeTrav'
            button_user.href = '/about/'
        }
    })
    .catch((error) => {
        console.log(error)
    })
})

if (url.searchParams.get('write_blog') == 'true') {
    if (authenticated) {
        form_blog.reset()
        blank(true)
        modal_blog(true)
    } else {
        userModal(
            'Cannot Write Blog',
            'Before write something in blog, you should login in ZeeTrav.',
            true
        )
    }
}

if (url.searchParams.get('login') == 'true') {
    form_login.style.display = 'block'
    form_register.style.display = 'none'
    document.querySelector('#login_username_email').focus()
}

if (url.searchParams.get('register') == 'true') {
    document.querySelector('#register_fullname').focus()
}

if (authenticated) {
    is_authenticated(authenticated)
}
