async function open_new_shift() {
    let can = await eel.data_get('a_status_raw')() === 1
    if (can)
        await eel.open_new_shift()()
}

async function close_shift(other_id) {
    let can = await eel.data_get('a_status_raw')() === 1
    if (can)
        await eel.close_shift(other_id)()
}

async function add_take(uid, place) {
    let can = await eel.data_get('a_status_raw')() === 1
    if (can)
        await eel.add_take(uid, place)()
}

async function close_take(take_pk) {
    let can = await eel.data_get('a_status_raw')() === 1
    if (can)
        await eel.close_take(take_pk)()
}