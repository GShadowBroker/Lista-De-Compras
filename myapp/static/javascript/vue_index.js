'use strict';

let app = new Vue({
    el: '#root',

    data: {
        message: '',
        messageEdit: '{{ item }}',
        className: { default: 'modal' },
    },

    methods: {
        ajax: function(url) {
            let xhttp = new XMLHttpRequest();

            xhttp.open('GET', url, true);

            xhttp.responseType = 'document';
        
            xhttp.onreadystatechange = function(){
        
                if (this.readyState == 4 && this.status == 200){

                    let xmlDoc = this.responseXML;
                    let text = document.querySelector('#test');

                    text.innerHTML = xmlDoc.querySelector('h1').textContent;
                }
            };
            
            xhttp.send();
        },

        sendOnEnter: function(event){
            if (event.keyCode == '13' && this.message){
                this.message = '';
            }
        },

    },

    delimiters: ['${', '}'],

    computed: {
        isDisabled(){
            if (this.message){
                return false;
            } else return true;
        },
    },
});

function areYouSure(event) {
    if (!confirm('Tem certeza de que deseja encerrar a sessão?')){
        event.preventDefault();
        return
    }
    return
}