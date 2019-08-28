<template>
    <v-container>
        <Userlist></Userlist>
    </v-container>
</template>

<script>
import Userlist from '@/components/user/UserList'
export default {
    name: "UserPage",
    components:{
        Userlist
    }
}
</script>

<style>
</style>