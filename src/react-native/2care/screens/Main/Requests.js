import React from 'react';
import { 
  View,
  Text,
  StyleSheet,
} from 'react-native';
import theme from '../../theme/theme.js'; 
import ResponsiveAppBar from '../../components/layout/ResponsiveAppBar.js';

export default function Requests({ navigation }) {
  const css = { backgroundColor: theme.palette.back_ground.light};
  return (
    <View> 
        <Text style={css}>Propostas</Text>
    </View>
  )
}