new Vue({
    el: '#tickets',
    data: {
        tickets: []
    },
    created: function () {
        const vm = this;
        const personal = document.location.search;
        axios.get('/tickets/api/tickets/' + personal)
            .then(function (response) {
                vm.tickets = response.data
                console.log(response.data)
//                console.log(personal)
            })
    }
});



