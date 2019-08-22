<template>
 <v-form ref="form">
   <v-layout>
     <v-flex xs2>
       <v-select :items="options" v-model="option"></v-select>
     </v-flex>
     <v-flex xs2>
       <v-select :items="checks" v-model="check"></v-select>
     </v-flex>
     <v-flex xs6>
       <v-text-field v-model="title" :label="optionLabel" />
     </v-flex>
   </v-layout>
   <v-layout justify-center pa-10>
     <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
   </v-layout>
 </v-form>
</template>
<script>
export default {
 props: {
   submit: {
     type: Function,
     default: () => {}
   }
 },
 data: () => ({
   title: "",
   genre: "",
   options: ['제목','장르'],
   option: "제목",
   checks: ['정렬','조회수순','평점순'],
   check: "정렬"
 }),
 computed: {
   optionLabel(){
     return "영화 "+this.option+"을/를 입력하세요"
   }
 },
 methods: {
   onSubmit: function() {
     var params = {};
     if(this.check == "정렬"){
       if(this.option == "제목"){
         params = {
           title:this.title
         };
       }
       else if(this.option == "장르"){
         params = {
           genre:this.title
         };
       }
     }else if(this.check == "조회수순"){
       if(this.option == "제목"){
         params = {
           title:this.title,
           order:"countrating"
         };
       }
       else if(this.option == "장르"){
         params = {
           genre:this.title,
           order:"countrating"
         };
       }
     }else if(this.check == "평점순"){
       if(this.option == "제목"){
         params = {
           title:this.title,
           order:"avgrating"
         };
       }
       else if(this.option == "장르"){
         params = {
           genre:this.title,
           order:"avgrating"
         };
       }
     }
     this.submit(params);
   }
 }
};
</script>
