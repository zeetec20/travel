import Axios from "axios"

let csrfmiddlewaretoken = document.querySelector('input[name="csrfmiddlewaretoken"]')
let form_subscribe = document.getElementById('form_subscribe')

form_subscribe.addEventListener('submit', (event) => {
    event.preventDefault()
    let data = new FormData(form_subscribe)
    Axios.post('/api/subscribe', data).then((response) => {
        console.log(response)
        form_subscribe.reset()
        if (response['data']['success']) {
            userModal(
                'Thank You for Subscribing',
                'After subscribing you will get information from an email',
                true
            )
        }
    })
    .catch((error) => {
        console.log(error)
    })
})

document.getElementById('modal-button-close').addEventListener('click', () => {
    console.log('test')
    userModal('', '', false)
})