let has_chosen = false;
let has_chosen_id = false;

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

    async function check_ticket_id() {
        await axios({
            method: 'get',
            url: '/tickets/api/checkticketid?id=' + chosen_ticket_id
        })
            .then(function (response) {
                console.log(response.data);
                has_chosen_id = response.data['has_chosen_id'];
                console.log(has_chosen_id)
            });
    };
    

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


    check_ticket_id();

    if (has_chosen == true) {
        alert('Вы уже выбрали тему. Второй раз выбрать тему или изменить свой выбор нельзя.');
    }
    else if (has_chosen_id == true) {
        alert('Кто-то уже выбрал эту тему. Обновите страницу и попробуйте еще раз.');
    }
    else {
        make_patch();
        location.href = '/tickets/confirmation';
    }
    
}

