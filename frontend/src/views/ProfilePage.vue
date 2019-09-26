<template>
    <v-container>
        <h1>회원 정보</h1>
        <v-btn to="/profileInfo" color="grey darken-2" class="white--text">개인 정보</v-btn>
        <v-btn to="/myRatingList" color="grey darken-2" class="white--text">내 평점 목록</v-btn>
        <router-view></router-view>
    </v-container>
</template>

<script>
export default {

}
</script>

<style>

</style>