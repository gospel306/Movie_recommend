<template>
    <v-container class="profile">
        <v-layout row wrap>
            <v-flex xs12 sm6 md12 lg4 xl2 class="board">
                <ProfileInfo></ProfileInfo>
            </v-flex>
            <v-flex xs12 sm6 md12 lg7 xl2 class="board">
                <MyRatingList></MyRatingList>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import ProfileInfo from "@/components/profile/ProfileInfo";
import MyRatingList from "@/components/profile/MyRatingList";

export default {
    components:{
        ProfileInfo,
        MyRatingList
    }
}
</script>

<style>
    .profile{
        /*background-color:tomato;*/
        height: 83%;
        width : 100%;
        border-radius: 50px;
    }
    .board{
        /*background-color:violet;*/
        margin-left : 20px;
        height: 580px;

    }
</style>