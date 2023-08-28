let has_chosen = false;

window.onload = function () {
    console.log('Готов!');

    const personal = document.location.search.replace('?', '');
    console.log(personal);

    async function check_ticket() {
        await axios({
            method: 'get',
            url: '/tickets/api/checktickets?personal=' + personal
        })
            .then(function (response) {
                console.log(response.data);
                has_chosen = response.data['has_chosen'];
                console.log(has_chosen)
            });
    };
    check_ticket();
};


function onClick() {
    const chosen_ticket_id = event.target.id.replace('b-', '');
    console.log(chosen_ticket_id);
    const personal = document.location.search.replace('?', '');
    console.log(personal);

    async function make_patch() {
        // const headers = { "X-CSRFTOKEN": "n0XfWS801fy1zLQpZBRltOE996pD4GN6" }
        await axios({
            method: 'patch',
            url: '/tickets/api/changeticket/' + chosen_ticket_id + '/',
            data: {
                "participant_cfl": personal,
                "is_available": 0
            },
            // headers: headers
        })
            .then(function (response) {
                console.log(response.data)
            });
    };

    if (has_chosen == true) {
        alert('Вы уже выбрали тему. Второй раз выбрать нельзя.');
    }
    else {
        make_patch();
        location.href = '/tickets/confirmation';
    }
    
}

