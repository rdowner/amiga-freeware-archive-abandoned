<template>
    <div>
        <div class="clearfix">
            <p class="display-1 float-right">#{{ disk.volume_number }}</p>
            <h1>{{ disk.name }}</h1>
            <p>{{ disk.description }}</p>
        </div>
        <div class="card-columns">
            <div v-for="artifact of disk.artifacts" v-bind:key="artifact.artifact_id">
                <ProductInfo v-bind:product="artifact"></ProductInfo>
            </div>
        </div>
    </div>
</template>

<script>
    import ProductInfo from './ProductInfo.vue'

    export default {
        name: 'DiskInfo',
        components: {
            ProductInfo
        },
        props: {
            disk: Object
        }
    }
</script>

<style scoped>
</style>