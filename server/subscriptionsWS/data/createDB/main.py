from flask import Flask, jsonify, request


from BLL.createDB import MembersBLL, MoviesBLL


app = Flask(__name__)


members = MembersBLL()
mem = members.insert_members()
print(mem)

movies = MoviesBLL()
mov = movies.insert_movies()
print(mov)

app.run()
