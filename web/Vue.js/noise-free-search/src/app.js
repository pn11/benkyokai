import Vue from 'vue'
//import BlockList from './block-list.vue';

Vue.component('block-list', {
    props: ['site'],
    template: 
        `<div>
        <input type="checkbox" v-model="site['doBlock']"> {{site.name}} <span v-if="site['doBlock'] === true"> : {{site.url}} is blocked.</span>
        </div>`
})
  

var app = new Vue({
    el: '#app',
    data: {
        search_button_name: 'Search with Google',
        message: 'Search query',
        sites: [
            {
                name: 'stackoverrun',
                url: 'stackoverrun.com',
                doBlock: true
            },
            {
                name: 'code.i-harness',
                url: 'code.i-harness.com',
                doBlock: true
            },
            {
                name: 'CODE Examples',
                url: 'code-examples.net',
                doBlock: true
            }
        ],
    },
    methods:{
    },
    computed: {
        search_query: function () {
            var query = "";
            this.sites.forEach(
                site => {
                    if (site.doBlock){
                        query += " -site:" + site.url;
                    }
                }
            );
            return query;
        }
    }
})