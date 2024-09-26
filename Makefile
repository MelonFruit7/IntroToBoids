EXE = boids

CC = g++
LIBS = -lraylib -ldl -lpthread -lX11 -lm
SRCS = Boids.cpp RealVector.cpp Boid.cpp

${EXE} : ${SRCS}
	${CC} ${SRCS} -o ${EXE} ${LIBS}