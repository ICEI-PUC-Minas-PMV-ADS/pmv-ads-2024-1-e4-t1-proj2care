import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';
import MaterialIcons from 'react-native-vector-icons/MaterialIcons';

import Home from '../screens/Main/Home';
import Search from '../screens/Main/Search';
import Profile from '../screens/Main/Profile';
import { useAuth } from '../contexts/AuthContext';
import UnsignedViews from './UnsignedViews';

const Tab = createBottomTabNavigator();
const Stack1 = createNativeStackNavigator();
const Stack2 = createNativeStackNavigator();
const Stack3 = createNativeStackNavigator();

const HomeStack = () => {
  return (
    <Stack1.Navigator initialRouteName="Home">
      <Stack1.Screen
        name="Home"
        component={Home}
        options={{
          headerShown: true,
          header: () => null,
        }}
      />
    </Stack1.Navigator>
  );
};

const RequestStack = () => {
  return (
    <Stack2.Navigator initialRouteName="RequestsCaregiver">
      <Stack2.Screen
        name="RequestsCaregiver"
        component={RequestsCaregiver}
        options={{
          headerShown: false,
          header: () => null,
        }}
      />
      <Stack2.Screen
        name="RequestsCareReceiver"
        component={RequestsCareReceiver}
        options={{
          header: () => null,
        }}
      />
      <Stack2.Screen
        name="SendRequest"
        component={SendRequest}
        options={{
          header: () => null,
        }}
      />
    </Stack2.Navigator>
  );
};

const ProfileStack = () => {
  return (
    <Stack3.Navigator initialRouteName="Profile">
      <Stack3.Screen
        name="Profile"
        component={Profile}
        options={{
          headerShown: false,
          header: () => null,
        }}
      />
    </Stack3.Navigator>
  );
};

const Main = () => {
  const { user } = useAuth();

  if (!user) {
    return <UnsignedViews />;
  }

  return (
    <Tab.Navigator
      initialRouteName="Home"
      screenOptions={{
        tabBarActiveTintColor: '#e91e63',
      }}
    >
      <Tab.Screen
        name="Home"
        component={HomeStack}
        options={{
          tabBarLabel: 'Home',
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="home" color={color} size={size} />
          ),
        }}
      />
      <Tab.Screen
        name="Search"
        component={Search}
        options={{
          tabBarLabel: 'Search',
          tabBarIcon: ({ color, size }) => (
            <MaterialIcons name="search" color={color} size={size} />
          ),
        }}
      />
      <Tab.Screen
        name="Profile"
        component={ProfileStack}
        options={{
          tabBarLabel: 'Profile',
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="account" color={color} size={size} />
          ),
        }}
      />
    </Tab.Navigator>
  );
};

export default Main;
