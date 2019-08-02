<template>
    <div id="app" class="container">
        <b-navbar type="light" variant="light" fixed="top" sticky="true">

            <b-navbar-brand to="/">
                <img id="amigalogo" alt="AMIGA" src="./assets/Amiga-Logo-1985.svg">
                Freeware Archive
            </b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-item-dropdown text="About" right>
                        <b-dropdown-item to="/about">About the Archive</b-dropdown-item>
                        <b-dropdown-item to="/about/bulk-downloads">Bulk Downloads</b-dropdown-item>
                        <b-dropdown-item to="/about/acceptable-use-policy">Acceptable Use Policy</b-dropdown-item>
                        <b-dropdown-item to="/about/privacy-policy">Privacy Policy</b-dropdown-item>
                    </b-nav-item-dropdown>

                    <b-nav-item-dropdown text="Browse" right>
                        <b-dropdown-item to="/libraries/fish">Fred Fish's Amiga Library Disks</b-dropdown-item>
                        <b-dropdown-item to="/libraries/17bit">17 Bit Software</b-dropdown-item>
                    </b-nav-item-dropdown>

                    <b-nav-item to="/search">Search</b-nav-item>
                </b-navbar-nav>
            </b-collapse>

        </b-navbar>

        <router-view></router-view>

        <div class="text-muted text-center small m-3">
            <hr/>
            <router-link to="/about/privacy-policy">Privacy Policy</router-link>
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
    a.unlink {
        color: inherit;
        text-decoration: inherit;
    }
    a.unlink:hover {
        color: inherit;
        text-decoration: inherit;
    }
</style>
