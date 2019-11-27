/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package crypto;

/**
 *
 * @author Mo Eltelawi
 */
public class RC4 {
    
    static int[] keys = new int[256];

    public static void intandgenk(String key) {

        int[] state = new int[256];

        //fill the state in keys array
        for (int i = 0; i < 256; i++) {
            state[i] = i;
            keys[i] = key.charAt(i % key.length());
        }
        //permutaion
        int j = 0;
        for (int i = 0; i < 256; i++) {
            j = (j + state[i] + keys[i]) % 256;
            int temp = state[i];
            state[i] = state[j];
            state[j] = temp;
        }
        //Generate keys
        int i = 0, index;
        j = 0;
        for (int x = 0; x < 256; x++) {
            i = (i + 1) % 256;
            j = (j + state[i]) % 256;
            int temp = state[i];
            state[i] = state[j];
            state[j] = temp;
            index = (state[i] + state[j]) % 256;
            keys[i] = state[index];
        }
    }

    public static String encryption(String plaintext) {

        String cipher = "";
        for (int i = 0; i < plaintext.length(); i++) {
            cipher += (char) (plaintext.charAt(i) ^ keys[i % keys.length]);
        }

        return cipher;
    }

    public static String decryption(String cipherText) {

        String decrypt = "";
        for (int i = 0; i < cipherText.length(); i++) {
            decrypt += (char) (cipherText.charAt(i) ^ keys[i % keys.length]);
        }

        return decrypt;
    }
    
}
