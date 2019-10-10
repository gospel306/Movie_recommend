<template>
    <v-container>
        <h1>관리자 페이지</h1>
        <v-btn to="/adminuser" color="grey darken-2" class="white--text">유저관리</v-btn>
        <v-btn to="/adminmovie" color="grey darken-2" class="white--text">영화관리</v-btn>
        <v-btn to="/cluster" color="grey darken-2" class="white--text">클러스터</v-btn>
        <v-btn to="/recommend" color="grey darken-2" class="white--text">DB관리</v-btn>
        <router-view></router-view>
    </v-container>
</template>

<script>
export default {

}
</script>

<style>

</style>