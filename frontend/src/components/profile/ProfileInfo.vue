<template>
  <v-container> 
    <v-layout column>
      <v-flex>
        <v-layout column>
          <v-flex>
            <h3>회원정보</h3>
          </v-flex>
          <v-flex>
            <v-layout row>
              <v-flex class="user-img">
                <div></div>
              </v-flex>
              <v-flex>
                <v-row>
                  <v-col>
                    <v-text-field v-model = "items.username"  label="Name" class="purple-input"/>
                    <v-text-field v-model = "items.gender"  label="Gender" class="purple-input"/>
                    <v-text-field v-model = "items.age"  label="Age" class="purple-input"/>
                    <v-text-field v-model = "items.occupation"  label="Job  " class="purple-input"/>                
                  </v-col>
                </v-row>

              </v-flex>  
            </v-layout>
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex>
        <div><h3>유사유저</h3></div>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import axios from "axios";
import router from '@/router';
export default {
  
  data() {
    return {
      items: []
    };
  },
  mounted() {
    axios
    .get(this.$store.state.server + "/api/users/?id=" + this.$session.get('id'))
    .then(res => {
      this.items = res.data;
    });    
  },
  methods: {
    modifyInfo: function(id){
      axios.put(
          this.$store.state.server + "/api/users/?id=" + id
          +"&gender="+this.items.gender
          +"&age="+this.items.age
          +"&occupation="+this.items.occupation
        )
        .then(() => {
          this.updateDialog = false;
          router.push("/profileInfo");
        });
    }
  }
};
</script>
<style>
  .head{
    background-color: blue;
  }
  .user-img{
    width:150px;
    height:300px;
    /*background: white;*/
    padding: 10px;
    margin-left : 30px;
  }
</style>
