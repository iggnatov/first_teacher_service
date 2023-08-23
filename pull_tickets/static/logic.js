new Vue({
    el: '#participants-table',
    data: {
        participants: []
    },
    created: function () {
        const pm = this;
        axios.get('/participants/api/participants/')
        .then(function (response) {
        pm.participants = response.data
        console.log(response.data)
        })
    }
});