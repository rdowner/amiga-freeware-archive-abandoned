<template>
    <div id="app" class="container">
        <div class="container">
            <h1 id="header">
                <img id="amigalogo" alt="AMIGA" src="./assets/Amiga-Logo-1985.svg">
                Freeware Archive
            </h1>
            <router-view></router-view>
            <router-link class="btn btn-primary" to="/">Go to home page</router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'app'
    }
</script>

<style lang="scss">
    @import 'assets/_custom.scss';
    @import '~bootstrap/scss/bootstrap.scss';
    @import '~bootstrap-vue/src/index.scss';

    #app {
    }

    #amigalogo {
        height: 1em;
    }
    #header {
        border-bottom: black solid thin;
    }
</style>
