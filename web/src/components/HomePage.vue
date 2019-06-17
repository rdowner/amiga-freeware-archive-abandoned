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
            <p>Please don't use crawlers or aggressive download managers. <router-link :to="{name:'bulk-downloads'}">We can provide bulk downloads</router-link> if you want them.</p>

        </b-jumbotron>

        <div class="card-columns">
            <b-card title="First card">
                <b-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras finibus in ligula sed efficitur. Quisque eros lacus, congue eget turpis vitae, sollicitudin viverra ante. Suspendisse semper, neque malesuada aliquam lacinia, neque turpis malesuada quam, vehicula efficitur risus velit vel urna. Ut et eros vitae felis egestas tincidunt. Donec nec eleifend orci. Sed eget tincidunt dui. In turpis urna, placerat ut consectetur eu, tincidunt quis odio. Morbi eget justo nec risus lobortis mattis in a sem. Donec mi elit, malesuada sed neque ac, dignissim lobortis dolor.</b-card-text>
            </b-card>
            <b-card title="Second card">
                <b-card-text>Cras ac semper justo, et faucibus ante. Aenean efficitur sagittis ultrices. Pellentesque vulputate pulvinar odio a ornare. Aenean eu efficitur mi, a pellentesque lectus. Donec consequat, dui eu auctor accumsan, mi erat lacinia lectus, quis ornare sem nibh id nunc. Proin sit amet vulputate lacus, et vulputate mauris. Ut dictum, urna vel tempor mollis, ipsum risus efficitur nulla, ut ullamcorper ligula tellus nec nisl. Nunc sit amet luctus ex. Integer quis elementum neque. Aenean et enim odio.</b-card-text>
            </b-card>
            <b-card title="Third card">
                <b-card-text>Suspendisse potenti. In molestie sollicitudin efficitur. Maecenas ut volutpat ex. Proin eu nunc in tellus maximus sollicitudin vel eget felis. Mauris vehicula turpis mauris, in vestibulum eros lobortis vel. Proin pulvinar eros at aliquet condimentum. Nam orci enim, lacinia vitae varius a, lobortis eu erat. Fusce quis pharetra metus. Quisque faucibus quam est, eu laoreet metus tincidunt nec.</b-card-text>
            </b-card>
        </div>

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
