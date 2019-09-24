<template>
  <v-container
    fill-height
    fluid
  > 
    <v-row justify="center">
      <v-col
        cols="12"
        md="8"
      >
        <material-card
          color="green"
          title="Edit Profile"
          text="Complete your profile"
        >
          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col
                  cols="2"
                  md="4"
                >
                  <v-text-field
                    v-model = "items.id"
                    label="User Name"
                    class="purple-input"
                  />
                </v-col>
                <v-col
                  cols="2"
                  md="4"
                >
                  <v-text-field
                    v-model = "items.gender"
                    label="Gender"
                    class="purple-input"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  cols="2"
                  md="4"
                >
                  <v-text-field
                    v-model = "items.age"
                    label="Age"
                    class="purple-input"
                  />
                </v-col>
                <v-col
                  cols="2"
                  md="4"
                >
                  <v-text-field
                    v-model = "items.occupation"
                    label="Occupation"
                    class="purple-input"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  cols="12"
                  class="text-right"
                >
                  <v-btn color="success" @click="modifyInfo($session.get('id'))">
                    Update Profile
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </material-card>
      </v-col>
    </v-row>
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
</style>
