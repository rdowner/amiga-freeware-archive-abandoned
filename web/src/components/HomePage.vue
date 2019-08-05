<template>
    <div>
        <b-jumbotron header="Search Free Amiga Software" v-bind:lead="leadText">

            <b-input-group class="mt-3" size="lg">
                <b-form-input placeholder="Search term" v-model="query"></b-form-input>
                <b-input-group-append>
                    <b-button v-on:click="search" variant="info">Search &gt;</b-button>
                </b-input-group-append>
            </b-input-group>

            <div class="text-muted">Looking for anti-virus? Try searching for <strong><router-link :to="{name:'search',query:{q:'virus killer'}}">virus killer</router-link></strong></div>
            <div class="text-muted">What software do we have by Carolyn Scheppner? <strong><router-link :to="{name:'search',query:{q:'author:scheppner'}}">author:scheppner</router-link></strong></div>
            <div class="text-muted">Need a better way to read text files? <strong><router-link :to="{name:'search',query:{q:'ppmore'}}">ppmore</router-link></strong></div>

        </b-jumbotron>

        <div class="text-center shadow p-3 mb-5 bg-white rounded">
            <p class="lead">
                The Amiga Freeware Archive aims to collect, catalog, and make available for search and download,<br/>
                the content of PD Libraries for classic Amiga computers.
            </p>
            <p><router-link to="/about" class="btn btn-primary" role="button">Learn More</router-link></p>
            <p class="text-muted small font-italic">
                We have an <router-link to="/about/acceptable-use-policy">Acceptable Use Policy</router-link> that asks
                <strong>please don't use Download Managers or Download Accelerators on this site</strong>. We use a very
                fast and reliable content delivery network which means you probably won't need one anyway. We also ask
                <strong>please don't use crawlers, scrapers, or bulk downloaders</strong> - instead, use our
                <router-link to="/about/bulk-downloads">bulk download interface</router-link> to get a fast and reliable
                download of all the site's content without pushing up the site's costs. Thank you for supporting the
                Amiga Freeware Archive by helping to keep our costs low!
            </p>
        </div>

        <!--<div>
            <h1 class="text-center">Browse the archive by PD Library</h1>
            <ul class="list-group list-group-horizontal text-center">
                <router-link to="/libraries/fish" class="list-group-item list-group-item-action">Fred Fish's Amiga Library Disks</router-link>
                <router-link to="/libraries/17bit" class="list-group-item list-group-item-action">17 Bit Software</router-link>
            </ul>
        </div>-->

    </div>
</template>

<script>
    export default {
        name: 'HomePage',
        data: function () {
            return {
                query: "", totaliser: -1
            }
        },
        methods: {
            search: function () {
                this.$router.push({ name: 'search', query: { q: this.query, page: 1 }});
            }
        },
        computed: {
            leadText: function() {
                return (this.totaliser < 0 ? 'Thousands of ' : this.totaliser + ' ') +
                        'downloads for the Commodore Amiga computer ready to be searched';
            }
        }
    }
</script>

<style scoped>
    .jumbotron {
        text-align: center;
    }
</style>
