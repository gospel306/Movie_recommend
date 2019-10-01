<template>
    <v-container class="profile">
        <v-layout row wrap>
            <v-flex xs12 sm6 md4 lg3 xl2 class="board">
                <h1>회원 정보</h1>
                <v-btn to="/profileInfo" color="grey darken-2" class="white--text">개인 정보</v-btn>
                <v-btn to="/myRatingList" color="grey darken-2" class="white--text">내 평점 목록</v-btn>
            </v-flex>
            <v-flex xs12 sm6 md4 lg3 xl2>
                <h1>평점 정보</h1>
                <v-btn to="/profileInfo" color="grey darken-2" class="white--text">개인 정보</v-btn>
                <v-btn to="/myRatingList" color="grey darken-2" class="white--text">내 평점 목록</v-btn>
            </v-flex>
        </v-layout>

    </v-container>
</template>

<script>
export default {

}
</script>

<style>
    .profile{
        background-color:tomato;
        height: 83%;
        width : 99%;
        border-radius: 50px;
    }
    .profile .board{
        background-color:violet;
        height : 5%;

    }
</style>