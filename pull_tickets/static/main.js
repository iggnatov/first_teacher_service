let has_chosen = false;

window.onload = function () {
    console.log('Готов!');

    const personal = document.location.search.replace('?', '');
    console.log('personal:', personal);

    async function check_ticket() {
        await axios({
            method: 'get',
            url: '/tickets/api/checktickets?personal=' + personal
        })
            .then(function (response) {
                console.log('response.data:', response.data);
                has_chosen = response.data['has_chosen'];
                console.log('has_chosen: ', has_chosen)
            });
    };
    check_ticket();
};


function onClick() {
    const chosen_ticket_id = event.target.id.replace('b-', '');
    console.log('chosen_ticket_id: ', chosen_ticket_id);
    const personal = document.location.search.replace('?', '');
    console.log('personal: ', personal);

    async function make_patch() {
        await axios({
            method: 'patch',
            url: '/tickets/api/changeticket/' + chosen_ticket_id + '/',
            data: {
                "participant_cfl": personal,
                "is_available": 0
            },
        })
            .then(function (response) {
                console.log(response.data)
            });
    };

    async function check_ticket_id() {
        await axios({
            method: 'get',
            url: '/tickets/api/checkticketid?id=' + chosen_ticket_id
        })
            .then(function (response) {
                console.log('response.data (check ticket id): ', response.data);
                is_ticket_available = response.data['is_ticket_available'];
                console.log('is_ticket_available: ', is_ticket_available);

                if (has_chosen == true) {
                    alert('Вы уже выбрали тему. Второй раз выбрать тему или изменить свой выбор нельзя.');
                }
                else if (is_ticket_available == false) {
                    alert('Кто-то уже выбрал эту тему. Обновите страницу и попробуйте еще раз.');
                }
                else {
                    make_patch();
                    location.href = '/tickets/confirmation';
                }
            });
    };
    check_ticket_id();
}

