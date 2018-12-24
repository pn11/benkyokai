var app = new Vue({
    el: '#app',
    data:{
        message: 'List of Fruits',
        fruit: ['apple', 'banana', 'strawberry']
    },
    methods:{
        addFruit(event, value){
            this.fruit.push(this.$refs.fruit_form.value)
            this.$refs.fruit_form.value = ''
        }
    }
})