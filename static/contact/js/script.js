import Axios from 'axios'

let form_message = document.querySelector('#form_message')

form_message.addEventListener('submit', (event) => {
    event.preventDefault()
    let data = new FormData(form_message)

    Axios.post('/api/message', data).then((response) => {
        console.log(response)
        if (response['data']['success'] == 'true') {
            userModal(
                'Thanks For Your Message',
                'Keep to monitor ZeeTrav to make your trip easier.',
                true
            )
        }
    })
    .catch((error) => {
        console.log(error)
    })
})