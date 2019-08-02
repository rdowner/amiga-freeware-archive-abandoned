<template>
    <div>
        <b-card v-bind:title="title" v-bind:sub-title="product.short">
            <b-card-text>
                <p v-if="product.description !== product.short">{{ product.description }}</p>
                <p v-if="product.author">Authored by <strong>{{ product.author }}</strong></p>
                <dl v-for="(v, k) in filtered" v-bind:key="k">
                    <dt>{{ k }}</dt>
                    <dd>{{ v }}</dd>
                </dl>
            </b-card-text>

            <b-button v-bind:href="downloadLink" variant="primary">Download</b-button>
        </b-card>
    </div>
</template>

<script>
    var filter = function( obj, predicate) {
        var result = {}, key;

        for (key in obj) {
            if (obj.hasOwnProperty(key) && !predicate(key)) {
                result[key] = obj[key];
            }
        }

        return result;
    };

    export default {
        name: 'ProductInfo',
        props: {
            product: Object
        },
        data: function(){
            return {
                filtered: filter(this.product, function(key){return key === "artifact_id"
                    || key === "filename"
                    || key === "disknumber"
                    || key === "content-type"
                    || key === "short"
                    || key === "name"
                    || key === "fullname"
                    || key === "description"
                    || key === "version"
                    || key === "author"
                    || key === "described-by"
                    ;}),
                title: (this.product.fullname ? this.product.fullname : this.product.name) + (this.product.version ? ' ' + this.product.version : ''),
                downloadLink: "/" + this.product.artifact_id
            };
        },
    }
</script>

<style scoped>
</style>