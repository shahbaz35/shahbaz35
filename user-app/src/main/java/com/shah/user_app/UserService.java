package com.shah.user_app;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    //save a new User
    public User saveUser(User user){
        return userRepository.save(user);
    }

    //find a user
    public Optional<User> findByUsername(String username){
        return userRepository.findByUsername(username);
    }

}
