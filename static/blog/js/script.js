import Axios from 'axios'


if (order_user != 'false' && like.value != 'true') {
    let form_blog_like = document.getElementById('form_blog_like')

    form_blog_like.addEventListener('submit', (event) => {
        if (order_user != 'false' && like.value != 'true') {
            document.querySelector('.count_like').innerHTML = Number(count_like.innerHTML) + 1
            document.querySelector('.buttonLike').style.color = 'tomato'
            document.querySelector('.count_like').style.color = 'tomato'
            event.preventDefault()
            let data = new FormData(form_blog_like)
            Axios.post('/api/blog/like', data).then((response) => {
                console.log(response['data'])
                like.value = 'true'
                document.querySelector('.buttonLike').setAttribute("for", "")
            })
            .catch(() => {

            })
        }
    })

}

document.querySelector('.buttonLike').addEventListener('click', ()=>{
    if (like.value == 'true') {
        let data = new FormData(document.getElementById('form_blog_unlike'))
        document.querySelector('.count_like').innerHTML = Number(count_like.innerHTML) - 1
        document.querySelector('.buttonLike').style.color = 'darkslategray'
        document.querySelector('.count_like').style.color = 'darkslategray'
        Axios.post('/api/blog/unlike', data).then((response)=>{
            console.log(response['data'])
            like.value = 'false'
            document.querySelector('.buttonLike').setAttribute("for", "submit_blog_liked")
        })
    }
})