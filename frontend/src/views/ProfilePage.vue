<template>
    <v-container class="profile">
        <v-layout row wrap>
            <v-flex sm5z class="board">
                <ProfileInfo></ProfileInfo>
            </v-flex>
            <v-flex sm5 class="board">
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
        height: 80%;
        width : 80%;

    }
    .board{
        /*background-color:violet;*/
        margin-left : 20px;
        height: 580px;

    }
</style>