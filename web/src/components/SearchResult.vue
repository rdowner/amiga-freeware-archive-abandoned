<template>
    <div style="position:relative">
        <b-link v-bind:href="hyperlink" class="stretched-link">
            <span class="font-weight-bold">
                    {{ title }} &bull; {{ product._source.short }}
            </span>
            <br/>
            <span class="text-muted">{{ hyperlink }}</span>
        </b-link>
        <p>
            <span v-if="description !== ''">{{ description }} &bull; </span>
            <span><span class="text-muted">relevance: {{ product._score }}</span></span>
        </p>
    </div>
</template>

<script>
    export default {
        name: 'SearchResult',
        props: {
            product: Object
        },
        computed: {
            title: function () {
                let fullname = this.product._source.fullname;
                let name = this.product._source.name;
                let version = this.product._source.version;
                return (fullname ? fullname : name) + (version ? ' ' + version : '')
            },
            description: function () {
                return (this.product._source.description !== this.product._source.short)
                    ? this.product._source.description
                    : '';
            },
            hyperlink: function () {
                let re = new RegExp('^libraries/(.+)/disks/(.+)/artifacts/(.+)$');
                let m = this.product._id.match(re);
                return '/libraries/' + m[1] + '/disks/' + m[2] + '#' + m[3];
            }
        }
    }
</script>

<style scoped>
</style>