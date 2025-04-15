async function fc_take(id) {
    await eel.fc_take(id)();
}

async function fc_ready(id) {
    await eel.fc_ready(id)();
}

async function fc_close(id) {
    await eel.fc_close(id)();
}

async function fc_create() {
    const val = (eid) => {
        console.log(eid)
        return document.getElementById(eid).value
    }
    await eel.fc_create(
        val('dish_name'),
        val('client_name'),
        val('weight'),
        val('cal'),
        val('ingredients'),
        val('comment'),
        val('extra_info'),
        val('price'),
        val('time_to_cook'),
    )()
}