package com.shah.user_app.Service;


import com.shah.user_app.Model.User;
import com.shah.user_app.dto.UserRegistrationDTO;
import com.shah.user_app.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    //save a new User
    public User saveUser(User user) {
        return userRepository.save(user);
    }

    //find a user
    public Optional<User> findByUsername(String username) {
        return userRepository.findByUsername(username);
    }

    public Optional<User> findByEmail(String email) {
        return userRepository.findByEmail(email);
    }

    public void registerNewUser(UserRegistrationDTO registrationDTO) {
        // Check if the username already exists
        Optional<User> existingUserByUsername = userRepository.findByUsername(registrationDTO.getUsername());
        if (existingUserByUsername.isPresent()) {
            throw new IllegalArgumentException("Username already exists.");
        }

        // Check if the email already exists
        Optional<User> existingUserByEmail = userRepository.findByEmail(registrationDTO.getEmail());
        if (existingUserByEmail.isPresent()) {
            throw new IllegalArgumentException("Email already exists.");
        }

        // Create a new User entity from the DTO
        User newUser = new User();
        newUser.setUsername(registrationDTO.getUsername());
        newUser.setPassword(registrationDTO.getPassword());  // Consider encoding the password
        newUser.setEmail(registrationDTO.getEmail());
        newUser.setRole("USER");  // Default role

        // Save the new user to the database
        userRepository.save(newUser);
    }

}
