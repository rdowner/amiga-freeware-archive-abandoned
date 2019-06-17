<template>
    <div>

        <b-input-group class="mt-3 mb-3" size="lg">
            <b-form-input placeholder="Search term" v-model="query"></b-form-input>
            <b-input-group-append>
                <b-button v-on:click="search" variant="info">Search &gt;</b-button>
            </b-input-group-append>
        </b-input-group>

        <div v-if="!ready" class="text-center">
            <b-spinner variant="primary" label="Searching..."></b-spinner>
        </div>

        <div v-if="ready">
            <div class="float-right">
                <b-pagination-nav :number-of-pages="totalPages" :link-gen="linkGen"></b-pagination-nav>
            </div>
            <p>Found <strong>{{ totalHits }}</strong> results. Showing results {{ startResult }} to {{ endResult }}:</p>
            <ol v-bind:start="startResult">
                <li v-for="item of searchHits" v-bind:key="item._id">
                    <SearchResult v-bind:product="item"></SearchResult>
                </li>
            </ol>
        </div>

    </div>
</template>

<script>
    import axios from 'axios'
    import SearchResult from './SearchResult.vue'

    export default {
        name: 'SearchPage',
        components: {
            SearchResult
        },
        data: function () {
            return {
                query: this.$route.query.q,
                page:  this.$route.query.page || 1,
                searchHits: [],
                totalHits: [],
                startResult: 0,
                endResult: 0,
                totalPages: 0,
                ready: false
            }
        },
        methods: {
            search: function () {
                let me = this;
                let from = ((me.page - 1) * 20);
                axios.get('/search?q=' + this.query + '&from=' + from)
                    .then(response => {
                        me.searchHits = response.data.result.hits.hits;
                        me.totalHits = response.data.result.hits.total;
                        me.startResult = from + 1;
                        me.endResult = Math.min(me.totalHits, ((me.page) * 20));
                        me.totalPages = Math.max(1, Math.ceil(me.totalHits / 20));
                        me.ready = true;
                    });
            },
            linkGen: function (pageNum) {
                return { name: 'search', query: { q: this.query, page: pageNum } }
            }
        },
        created: function() { this.search(); }
    }
</script>

<style scoped>
</style>
