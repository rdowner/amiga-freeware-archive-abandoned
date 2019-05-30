<template>
    <div>
        <h1>{{ product.name }}</h1>
        <h2>{{ product.short }}</h2>
        <p>{{ product.description }}</p>
        <dl v-for="(v, k) in filtered" v-bind:key="k">
            <dt>{{ k }}</dt>
            <dd>{{ v }}</dd>
        </dl>
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
                filtered: filter(this.product, function(key){return key == "artifact_id"
                    || key == "filename"
                    || key == "disknumber"
                    || key == "content-type"
                    || key == "short"
                    || key == "name"
                    || key == "description"
                    ;})
            };
        },
    }
</script>

<style scoped>
</style>