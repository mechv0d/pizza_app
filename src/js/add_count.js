async function add_count(element) {
    let count = await eel.add_count()()
    console.log(count)
    element.innerText = `Счёт: ${count}`
}