// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Todo {
    struct Task {
        uint id;
        string description;
        bool completed;
    }

    mapping(uint => Task) public tasks;
    uint public nextId;

    function createTask(string memory _description) public {
        tasks[nextId] = Task(nextId, _description, false);
        nextId++;
    }

    function toggleTask(uint _id) public {
        tasks[_id].completed = !tasks[_id].completed;
    }

    function getTask(uint _id) public view returns (uint, string memory, bool) {
        Task memory t = tasks[_id];
        return (t.id, t.description, t.completed);
    }
}
