async function add_count(element) {
    let count = await eel.add_count()()
    let p = document.querySelector('#count')
    console.log(count)
    p.innerText = `Счёт: ${count}`
}