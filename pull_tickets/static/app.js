new Vue({
    el: '#tickets',
    data: {
    tickets: []
    },
    created: function () {
        const vm = this;
        axios.get('/tickets/api/tickets/')
        .then(function (response) {
        vm.tickets = response.data
        console.log(response.data)
        })
    }
})