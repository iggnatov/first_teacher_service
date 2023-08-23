new Vue({
    el: '#app',
    data() {
        return {
            topics: [
                { id: 'T1', name: 'Тема 1', description: 'Описание вопроса 1', available: true },
                { id: 'T2', name: 'Тема 2', description: 'Описание вопроса 2', available: true },
                { id: 'T3', name: 'Тема 3', description: 'Описание вопроса 3', available: true },
                { id: 'T4', name: 'Тема 4', description: 'Описание вопроса 4', available: true },
                { id: 'T5', name: 'Тема 5', description: 'Описание вопроса 5', available: true },
                { id: 'T6', name: 'Тема 6', description: 'Описание вопроса 6', available: true },
                { id: 'T7', name: 'Тема 7', description: 'Описание вопроса 7', available: true },
                { id: 'T8', name: 'Тема 8', description: 'Описание вопроса 8', available: true },
                { id: 'T9', name: 'Тема 9', description: 'Описание вопроса 9', available: true },
                { id: 'T10', name: 'Тема 10', description: 'Описание вопроса 10', available: true },
                { id: 'T11', name: 'Тема 11', description: 'Описание вопроса 11', available: true },
                { id: 'T12', name: 'Тема 12', description: 'Описание вопроса 12', available: true },
                { id: 'T13', name: 'Тема 13', description: 'Описание вопроса 13', available: true },
                { id: 'T14', name: 'Тема 14', description: 'Описание вопроса 14', available: true },
                { id: 'T15', name: 'Тема 15', description: 'Описание вопроса 15', available: true },
                { id: 'T16', name: 'Тема 16', description: 'Описание вопроса 16', available: true },
                { id: 'T17', name: 'Тема 17', description: 'Описание вопроса 17', available: true },
                { id: 'T18', name: 'Тема 18', description: 'Описание вопроса 18', available: true },
                { id: 'T19', name: 'Тема 19', description: 'Описание вопроса 19', available: true },
                { id: 'T20', name: 'Тема 20', description: 'Описание вопроса 20', available: true },
                { id: 'T21', name: 'Тема 21', description: 'Описание вопроса 21', available: true },
                { id: 'T22', name: 'Тема 22', description: 'Описание вопроса 22', available: true },
                { id: 'T23', name: 'Тема 23', description: 'Описание вопроса 23', available: true },
                { id: 'T24', name: 'Тема 24', description: 'Описание вопроса 24', available: true },
                { id: 'T25', name: 'Тема 25', description: 'Описание вопроса 25', available: true },
                { id: 'T26', name: 'Тема 26', description: 'Описание вопроса 26', available: true },
                { id: 'T27', name: 'Тема 27', description: 'Описание вопроса 27', available: true },
                { id: 'T28', name: 'Тема 28', description: 'Описание вопроса 28', available: true },
                { id: 'T29', name: 'Тема 29', description: 'Описание вопроса 29', available: true },
                { id: 'T30', name: 'Тема 30', description: 'Описание вопроса 30', available: true },
                { id: 'T31', name: 'Тема 31', description: 'Описание вопроса 31', available: true },
                { id: 'T32', name: 'Тема 32', description: 'Описание вопроса 32', available: true },
                { id: 'T33', name: 'Тема 33', description: 'Описание вопроса 33', available: true },
                { id: 'T34', name: 'Тема 34', description: 'Описание вопроса 34', available: true },
                { id: 'T35', name: 'Тема 35', description: 'Описание вопроса 35', available: true },
                { id: 'T36', name: 'Тема 36', description: 'Описание вопроса 36', available: true },
                { id: 'T37', name: 'Тема 37', description: 'Описание вопроса 37', available: true },
                { id: 'T38', name: 'Тема 38', description: 'Описание вопроса 38', available: true },
                { id: 'T39', name: 'Тема 39', description: 'Описание вопроса 39', available: true },
                { id: 'T40', name: 'Тема 40', description: 'Описание вопроса 40', available: true },
            ],
            chosenTopic: null,
            isModalVisible: false,
            participantCode: "",
            topicValue: "",
        };
    },
    computed: {
        hasChosenTopic() {
            return !!this.chosenTopic;
        }
    },
    methods: {
        selectTopic(topic) {
            this.chosenTopic = topic;
           this.showModal();
            },
         showModal() {
      this.isModalVisible = true;
    },

    cancelTopic() {
        this.chosenTopic = null;
        this.hideModal();
    },

    hideModal() {
        this.isModalVisible = false;      
        const modalBackdrop = document.getElementsByClassName("modal-backdrop");
        if (modalBackdrop[0]) {
            modalBackdrop[0].parentNode.removeChild(modalBackdrop[0]);
        }
        document.body.classList.remove("modal-open");
    },
    confirmTopic() {
        const selectedTopic = this.chosenTopic;
        const url = `https://my-school.online/tickets/api/tickets?code=${this.participantCode}&topic=${selectedTopic.id}`;
    alert(url);
    this.topics = this.topics.map((t) => {
      if (t.id === selectedTopic.id) {
        return { ...t, available: false };
      } else {
        return t;
      }
    });
    this.hideModal(); 
    },
    
    extractParamsFromURL(url) {
      const params = new URLSearchParams(new URL(url).search);
      this.participantCode = params.get("code");
      this.topicValue = params.get("topic");
    }
},
    mounted() {
        //alert(window.location.href);
    
        const exampleURL = "https://my-school.online/tickets/api/tickets?code=2000123&topic=1";
        this.extractParamsFromURL(exampleURL);
        // В результате, this.participantCode будет равен '2000123', а this.topicValue будет равен '1'
    
        //Нужно обновление страницы до актуального перечня тем
        //  setInterval(() => {
        //   this.topics = this.topics.map((t) => {
        //     if (t.id === topic.id) {
        //         return { ...t, available: false };
        //     } else {
        //         return t;
        //     }
        // });
        // }, 200);
      }
});
