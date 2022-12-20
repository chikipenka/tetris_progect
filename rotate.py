def rotate():
    if event.key == pygame.K_n:
        right_rotate_trigger = True
        if figure_list[-1][0].type == 'stick':
            if figure_list[-1][0].orientation % 4 == 1:
                if collision_list[
                    figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1] + 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0]][
                    figure_list[-1][0].coordinates[1][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 2][
                            figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1] + 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 0:
                print(figure_list[-1][0].coordinates[0][0] + 3)
                if collision_list[figure_list[-1][0].coordinates[0][0] + 3][
                    figure_list[-1][0].coordinates[0][1] + 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1] + 1] == 1 or collision_list[
                    figure_list[-1][0].coordinates[3][0]][
                    figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1] + 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[
                    figure_list[-1][0].coordinates[0][0] + 3][
                    figure_list[-1][0].coordinates[0][1] - 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0]][
                            figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1] - 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[
                    figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1] - 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0]][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 2][
                            figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1] - 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]

        if figure_list[-1][0].type == 'right_l_figure':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 1][
                    figure_list[-1][0].coordinates[0][1] - 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0] + 1][
                            figure_list[-1][0].coordinates[2][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0] + 1][
                            figure_list[-1][0].coordinates[2][1] + 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0],
                                                         figure_list[-1][0].coordinates[0][1] - 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 3][
                    figure_list[-1][0].coordinates[0][1]] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0] + 2][
                            figure_list[-1][0].coordinates[1][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0]][
                            figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1]]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 1][
                    figure_list[-1][0].coordinates[0][1] + 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0]][
                            figure_list[-1][0].coordinates[1][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 2][
                            figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0],
                                                         figure_list[-1][0].coordinates[0][1] + 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 1:
                if collision_list[figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1]] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0]][
                            figure_list[-1][0].coordinates[1][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 2][
                            figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1]]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
        if figure_list[-1][0].type == 'left_l_figure':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[figure_list[-1][0].coordinates[3][0] - 1][
                    figure_list[-1][0].coordinates[3][1]] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0]][
                            figure_list[-1][0].coordinates[2][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[0][0] + 2][
                            figure_list[-1][0].coordinates[0][1] - 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 1,
                                                         figure_list[-1][0].coordinates[0][1] - 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] - 1,
                                                         figure_list[-1][0].coordinates[2][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 2,
                                                         figure_list[-1][0].coordinates[3][1]]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 2][
                    figure_list[-1][0].coordinates[0][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0]][
                            figure_list[-1][0].coordinates[2][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 1][
                            figure_list[-1][0].coordinates[3][1] - 2] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 1,
                                                         figure_list[-1][0].coordinates[0][1] + 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] - 1,
                                                         figure_list[-1][0].coordinates[2][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0],
                                                         figure_list[-1][0].coordinates[3][1] - 2]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1]] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0] + 2][
                            figure_list[-1][0].coordinates[2][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 3][
                            figure_list[-1][0].coordinates[3][1]] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 1,
                                                         figure_list[-1][0].coordinates[0][1] + 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] + 1,
                                                         figure_list[-1][0].coordinates[2][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 2,
                                                         figure_list[-1][0].coordinates[3][1]]
            elif figure_list[-1][0].orientation % 4 == 1:
                if collision_list[figure_list[-1][0].coordinates[0][0]][
                    figure_list[-1][0].coordinates[0][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0] + 2][
                            figure_list[-1][0].coordinates[2][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 1][
                            figure_list[-1][0].coordinates[3][1] + 2] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 1,
                                                         figure_list[-1][0].coordinates[0][1] - 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] + 1,
                                                         figure_list[-1][0].coordinates[2][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0],
                                                         figure_list[-1][0].coordinates[3][1] + 2]
        if figure_list[-1][0].type == 't_figure':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 1][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    t = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = [t[0] - 1, t[1] - 1]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[figure_list[-1][0].coordinates[1][0]][figure_list[-1][0].coordinates[1][1]] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    t = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = [t[0] + 1, t[1] - 1]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 1][
                    figure_list[-1][0].coordinates[1][1] + 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    t = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = [t[0] + 1, t[1] + 1]
            elif figure_list[-1][0].orientation % 4 == 1:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 2][figure_list[-1][0].coordinates[1][1]] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    t = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = [t[0] - 1, t[1] + 1]

    elif event.key == pygame.K_m:
        # вращение против часовой стрелки
        left_rotate_trigger = True
        if figure_list[-1][0].type == 'stick':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[
                    figure_list[-1][0].coordinates[0][0] + 3][
                    figure_list[-1][0].coordinates[0][1] - 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1 or collision_list[
                    figure_list[-1][0].coordinates[3][0]][
                    figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1] - 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
            elif figure_list[-1][0].orientation % 4 == 1:
                print(figure_list[-1][0].coordinates[0][0] + 3)
                if collision_list[figure_list[-1][0].coordinates[0][0] + 3][
                    figure_list[-1][0].coordinates[0][1] + 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1] + 1] == 1 or collision_list[
                    figure_list[-1][0].coordinates[3][0]][
                    figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1] + 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[
                    figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1] + 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0]][
                    figure_list[-1][0].coordinates[1][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 2][
                            figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1] + 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[
                    figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1] - 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0]][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 2][
                            figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1] - 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
        if figure_list[-1][0].type == 'right_l_figure':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 3][
                    figure_list[-1][0].coordinates[0][1]] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0] + 2][
                            figure_list[-1][0].coordinates[1][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0]][
                            figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1]]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 1:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 1][
                    figure_list[-1][0].coordinates[0][1] - 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0] + 2][
                            figure_list[-1][0].coordinates[1][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0]][
                            figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0],
                                                         figure_list[-1][0].coordinates[0][1] - 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1]] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0]][
                            figure_list[-1][0].coordinates[1][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 2][
                            figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1]]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 1][
                    figure_list[-1][0].coordinates[0][1] + 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0]][
                            figure_list[-1][0].coordinates[1][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 2][
                            figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0],
                                                         figure_list[-1][0].coordinates[0][1] + 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]

        left_rotate_trigger = True
        if figure_list[-1][0].type == 'left_l_figure':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 2][
                    figure_list[-1][0].coordinates[0][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0]][
                            figure_list[-1][0].coordinates[2][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 1][
                            figure_list[-1][0].coordinates[3][1] - 2] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 1,
                                                         figure_list[-1][0].coordinates[0][1] + 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] - 1,
                                                         figure_list[-1][0].coordinates[2][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0],
                                                         figure_list[-1][0].coordinates[3][1] - 2]
            elif figure_list[-1][0].orientation % 4 == 1:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 2][
                    figure_list[-1][0].coordinates[0][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0]][
                            figure_list[-1][0].coordinates[2][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] - 1][
                            figure_list[-1][0].coordinates[3][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 1,
                                                         figure_list[-1][0].coordinates[0][1] - 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] - 1,
                                                         figure_list[-1][0].coordinates[2][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 2,
                                                         figure_list[-1][0].coordinates[3][1]]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[figure_list[-1][0].coordinates[0][0]][
                    figure_list[-1][0].coordinates[0][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0] + 2][
                            figure_list[-1][0].coordinates[2][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 1][
                            figure_list[-1][0].coordinates[3][1] + 2] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 1,
                                                         figure_list[-1][0].coordinates[0][1] - 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] + 1,
                                                         figure_list[-1][0].coordinates[2][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0],
                                                         figure_list[-1][0].coordinates[3][1] + 2]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[figure_list[-1][0].coordinates[0][0]][
                    figure_list[-1][0].coordinates[0][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0] + 2][
                            figure_list[-1][0].coordinates[2][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 3][
                            figure_list[-1][0].coordinates[3][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 1,
                                                         figure_list[-1][0].coordinates[0][1] + 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] + 1,
                                                         figure_list[-1][0].coordinates[2][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 2,
                                                         figure_list[-1][0].coordinates[3][1]]

        if figure_list[-1][0].type == 't_figure':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 1][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    t = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = [t[0] + 1, t[1] - 1]
            elif figure_list[-1][0].orientation % 4 == 1:
                if collision_list[figure_list[-1][0].coordinates[1][0]][
                    figure_list[-1][0].coordinates[1][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    t = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = [t[0] - 1, t[1] - 1]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 1][
                    figure_list[-1][0].coordinates[1][1] + 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    t = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = [t[0] - 1, t[1] + 1]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    t = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = [t[0] + 1, t[1] + 1]

    if event.key == pygame.K_m or event.key == pygame.K_n:
        left_rotate_trigger = True
        if figure_list[-1][0].type == 'left_z_figure':
            if figure_list[-1][0].orientation % 2 == 0:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 1][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[0][0] + 1][
                            figure_list[-1][0].coordinates[0][1] + 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0],
                                                         figure_list[-1][0].coordinates[2][1] - 2]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 2,
                                                         figure_list[-1][0].coordinates[3][1]]
            else:
                if collision_list[figure_list[-1][0].coordinates[2][0] + 1][
                    figure_list[-1][0].coordinates[2][1] + 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 3][
                            figure_list[-1][0].coordinates[3][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0],
                                                         figure_list[-1][0].coordinates[2][1] + 2]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 2,
                                                         figure_list[-1][0].coordinates[3][1]]
        if figure_list[-1][0].type == 'right_z_figure':
            if figure_list[-1][0].orientation % 2 == 0:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 1][
                    figure_list[-1][0].coordinates[1][1] - 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[0][0] + 3][
                            figure_list[-1][0].coordinates[0][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1]]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0],
                                                         figure_list[-1][0].coordinates[1][1] - 2]
            else:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 1][
                    figure_list[-1][0].coordinates[1][1] + 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[0][0] - 1][
                            figure_list[-1][0].coordinates[0][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1]]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0],
                                                         figure_list[-1][0].coordinates[1][1] + 2]
