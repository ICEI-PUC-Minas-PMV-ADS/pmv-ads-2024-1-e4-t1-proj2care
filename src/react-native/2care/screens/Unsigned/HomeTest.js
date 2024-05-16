import React, { createContent, useContext, useState } from "react";
import { View, Text, StyleSheet, Image, Pressable } from "react-native";
import theme from "../../theme/theme.js";
import { logout } from "../../services/authServiceMob.js";

export default function HomeTest({ navigation }) {

  
  const handleLogout = async () => {
    const navigateToLogin = () => {
      console.log("Usuário deslogado");
      navigation.navigate('Login'); 
    };
    await logout(navigateToLogin);
  };

  return (
    <View>    
      <View style={styles.logo}>
        <Image
          source={require("../../assets/logo2care.png")}
          style={styles.logoImg}
        />
      </View>
      <View style={styles.userLogged}>
        <Text style={styles.textUserLogged}>
          Você está na HomeTest do App 2Care
        </Text>
      </View>

      <Pressable
        onPress={handleLogout} 
        style={({ pressed }) => [
          styles.buttonUser,
          pressed && { transform: [{ scale: 1.1 }] },
        ]}
      >
        <Text style={styles.buttonUserText}>Logout</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  containerRegister: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    width: "80%",
    marginLeft: "10%",
    marginRight: "10%",
  },
  logo: {
    alignItems: "center",
    marginTop: "auto",
  },
  userLogged: {
    justifyContent: "center",
    alignItems: "center",
  },
  textUserLogged: {
    fontSize: 20,
  },
  buttonUser: {
    backgroundColor: "#FF5733",
    padding: 10,
    borderRadius: 25,
    width: 170,
    margin: "auto",
    justifyContent: "center",
  },
  buttonUserText: {
    color: "#FFFFFF",
    textAlign: "center",
    margin: "auto",
    fontSize: 20,
  },
});
