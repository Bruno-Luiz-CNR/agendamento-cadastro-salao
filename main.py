from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from ui_main import Ui_MainWindow
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
import sqlite3

banco = sqlite3.connect('salao.db')

cursor = banco.cursor()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("BruTha - Sistema de cadastro e agendamento")
        appIcon = QIcon(u"img/recrutamento.png")
        self.setWindowIcon(appIcon)

        self.tableWidget_2.setColumnWidth(0, 10)
        self.tableWidget_2.setColumnWidth(1, 220)
        self.tableWidget_2.setColumnWidth(2, 100)
        self.tableWidget_2.setColumnWidth(3, 150)
        self.tableagehora.setColumnWidth(0, 10)
        self.tableagehora.setColumnWidth(1, 220)
        self.tableagehora.setColumnWidth(2, 100)
        self.tableagehora.setColumnWidth(3, 100)
        self.tableagehora.setColumnWidth(5, 50)
        self.tableagehora.setColumnWidth(6, 50)
        self.tabelapromoes.setColumnWidth(0, 10)
        self.tabelapromoes.setColumnWidth(1, 220)
        self.tabelapromoes.setColumnWidth(2, 100)
        self.tabelaestoque.setColumnWidth(0, 10)
        self.tabelaestoque.setColumnWidth(1, 220)
        self.tabelaestoque.setColumnWidth(2, 100)
        self.tabelaestoque.setColumnWidth(3, 100)
        self.tabelaestoque.setColumnWidth(4, 50)
        self.tableWidget_3.setColumnWidth(0, 10)
        self.tableWidget_3.setColumnWidth(1, 220)
        self.tableWidget_3.setColumnWidth(2, 100)
        self.tableWidget_3.setColumnWidth(3, 100)
        self.tableWidget_3.setColumnWidth(4, 100)
        self.tableWidget_3.setColumnWidth(5, 60)

        self.btn_toogle.clicked.connect(self.leftMenu)
        self.btn_toogle.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        # botões de menu lateral
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_cadastro.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cad))
        self.btn_agenda.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_agend))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
        self.btn_consulestoque.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_consul))
        self.btn_promo.clicked.connect(lambda: self.pages.setCurrentWidget(self.pagepromo))
        # botao gravar cadastro de cliente
        self.btn_inccli.clicked.connect(self.btn)
        self.btn_inccli.clicked.connect(self.tabepromo)
        self.btn_inccli.clicked.connect(self.buscar_empresas)
        self.btn_pescliente.clicked.connect(self.pesquisarcliente)
        self.btn_pesqini.clicked.connect(self.pesqdata)
        self.btn_pesqini.clicked.connect(self.pesqdata)
        # buscando dados mysql
        self.buscar_empresas()
        # excluir
        self.tableWidget_2.clicked.connect(self.selecaocli)
        self.btn_exccli.clicked.connect(self.excluir)
        self.btn_exccli.clicked.connect(self.tabepromo)
        self.btn_exccli.clicked.connect(self.buscar_empresas)
        # inclui funcionario
        self.buscarfun()
        self.btn_incfun.clicked.connect(self.btninclu)
        self.btn_incfun.clicked.connect(self.funciona)
        self.btn_incfun.clicked.connect(self.funcionahora)
        self.btn_incfun.clicked.connect(self.buscarfun)
        self.btn_excfun.clicked.connect(self.exccfun)
        self.btn_excfun.clicked.connect(self.funcionahora)
        self.btn_excfun.clicked.connect(self.funciona)
        self.btn_excfun.clicked.connect(self.buscarfun)
        self.btn_altfun.clicked.connect(self.altefun)
        self.btn_altfun.clicked.connect(self.funciona)
        self.btn_altfun.clicked.connect(self.funcionahora)
        self.btn_altfun.clicked.connect(self.buscarfun)
        self.tableWidget.clicked.connect(self.selecaofun)
        # agendamento
        self.btn_agendar.clicked.connect(self.incage)
        self.btn_agendar.clicked.connect(self.tabelaagen)
        self.tableagehora.clicked.connect(self.tabelaagehora)
        self.btn_agendar.clicked.connect(self.tabelahora)
        self.funciona()
        self.tabelaagen()
        self.pesquisarvaloresagenda()
        self.btn_pescli.clicked.connect(self.pesquisaragendamento)
        self.btn_pesval.clicked.connect(self.pesquisarvaloresagenda)
        self.btn_excagend.clicked.connect(self.excluiragenda)
        self.btn_excagend.clicked.connect(self.tabelaagen)
        self.btn_excagend.clicked.connect(self.buscarvaloragenda)
        self.btn_excagend.clicked.connect(self.tabelahora)
        self.tableWidget_3.clicked.connect(self.buscaragenda)
        self.pushButton.clicked.connect(self.altefunagenda)
        self.pushButton.clicked.connect(self.tabelaagen)
        self.pushButton.clicked.connect(self.tabelahora)

        # horario de agemdamento
        self.tabelahorario()
        self.pesfuncio2()
        self.pesqfunhora()
        self.btn_agendhora.clicked.connect(self.inclhora)
        self.btn_agendhora.clicked.connect(self.buscarvaloragenda)
        self.btn_agendhora.clicked.connect(self.tabelahorario)
        self.btn_agendhora.clicked.connect(self.tabelaagen)
        self.btn_agendhora.clicked.connect(self.pesfuncio2)
        self.btn_althora.clicked.connect(self.altehora)
        self.btn_althora.clicked.connect(self.tabelaagen)
        self.btn_althora.clicked.connect(self.pesfuncio2)
        self.btn_althora.clicked.connect(self.tabelaagen)
        self.btn_althora.clicked.connect(self.tabelahorario)
        self.btn_excagendhora.clicked.connect(self.tabelaagen)
        self.btn_excagendhora.clicked.connect(self.exchora)
        self.btn_excagendhora.clicked.connect(self.tabelahorario)
        self.btn_excagendhora.clicked.connect(self.buscarvaloragenda)
        self.btn_pesclihora.clicked.connect(self.pesclihora)
        self.btn_pesvalhora.clicked.connect(self.pesfuncio2)

        # ESTOQUE
        self.tabestoque()
        self.valprodutostotal()
        self.btn_inclestoq.clicked.connect(self.incluestoque)
        self.btn_inclestoq.clicked.connect(self.valprodutostotal)
        self.btn_inclestoq.clicked.connect(self.tabestoque)
        self.tabelaestoque.clicked.connect(self.buscarprodutostabela)
        self.btn_altestoque.clicked.connect(self.alprodutos)
        self.btn_altestoque.clicked.connect(self.valprodutostotal)
        self.btn_altestoque.clicked.connect(self.tabestoque)
        self.btn_exclestoq.clicked.connect(self.excluirestoque)
        self.btn_exclestoq.clicked.connect(self.tabestoque)
        self.btn_exclestoq.clicked.connect(self.valprodutostotal)
        self.btn_pesqestoq.clicked.connect(self.pescpro)
        # promoção
        self.tabepromo()
        self.btn_envipromo.clicked.connect(self.enviarpromocao)

    def btninclu(self):
        nomcli = self.txt_nomcadfun.text()
        endcli = self.txt_endcadfun.text()
        telcli = self.txt_telcadfun.text()
        if nomcli != "" and endcli != "" and telcli != "":
            commando = f'INSERT INTO cadfun (nome, telefone, endereco) VALUES ("{nomcli}", "{telcli}", "{endcli}")'
            cursor.execute(commando)
            banco.commit()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro de Funcionário")
            msg.setText("Cadastro Realizado com Sucesso")
            msg.exec()

            self.txt_nomcadcli.setText("")
            self.txt_endcadcli.setText("")
            self.txt_telcadcli.setText("")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Cadastro de Funcionário")
            msg.setText("Cadastro Incompleto, preecha as informações")
            msg.exec()

    def btn(self):
        nomcli = self.txt_nomcadcli.text()
        endcli = self.txt_endcadcli.text()
        telcli = self.txt_telcadcli.text()
        if nomcli != "" and endcli != "" and telcli != "":
            commando = f'INSERT INTO cadastro (nome_cl, endereco_cl, telcli) VALUES ("{nomcli}", "{endcli}", ' \
                        f'"{telcli}")'
            cursor.execute(commando)
            banco.commit()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro de Cliente")
            msg.setText("Cadastro Realizado com Sucesso")
            msg.exec()

            self.txt_nomcadcli.setText("")
            self.txt_endcadcli.setText("")
            self.txt_telcadcli.setText("")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Cadastro de Cliente")
            msg.setText("Cadastro Incompleto, preecha as informações")
            msg.exec()

    def pesquisarcliente(self):
        pesquisa = self.txt_pescli.text()
        consulta = f"select id, nome_cl, telcli, endereco_cl from cadastro where " \
                   f"nome_cl like '%{pesquisa}%' or nome_cl like '%{pesquisa}%'"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        if not linhas:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Pesquisa de cliente")
            msg.setText("Nome encontrado")
            msg.exec()
        else:
            self.tableWidget_2.clearContents()
            self.tableWidget_2.setRowCount(len(linhas))
            for row, text in enumerate(linhas):
                for column, data in enumerate(text):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(data)))

    def excluir(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excluir Cadastro")
        msg.setText("Voce tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        ids = self.tableWidget_2.selectionModel().currentIndex().siblingAtColumn(0).data()
        if ids is not None:
            if resp == QMessageBox.Yes:
                banco.cursor()
                commando = f'DELETE FROM cadastro WHERE id = {ids}'
                cursor.execute(commando)
                banco.commit()
                self.txt_telcadcli.setText("")
                self.txt_endcadcli.setText("")
                self.txt_nomcadcli.setText("")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Cadastro de Cliente")
            msg.setText("Favor selecione o cliente para ser excluido")
            msg.exec()

    def exccfun(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excluir Funcionário")
        msg.setText("Voce tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        ids = self.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
        if ids is not None:
            if resp == QMessageBox.Yes:
                banco.cursor()
                commando = f'DELETE FROM cadfun WHERE id = {ids}'
                cursor.execute(commando)
                banco.commit()
                self.txt_nomcadfun.setText("")
                self.txt_endcadfun.setText("")
                self.txt_telcadfun.setText("")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Cadastro de Funcionário")
            msg.setText("Favor selecione o cliente para ser excluido")
            msg.exec()

    def altefun(self):
        nomfun = self.txt_nomcadfun.text()
        endfun = self.txt_endcadfun.text()
        telfun = self.txt_telcadfun.text()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excluir Cadastro")
        msg.setText("Voce tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()
        ids = self.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
        if resp == QMessageBox.Yes:
            if nomfun != "" and endfun != "" and telfun != "" and (ids is not None):
                commando = f'UPDATE cadfun SET nome = "{nomfun}", ' \
                            f'telefone = "{telfun}", ' \
                            f'endereco = "{endfun}" ' \
                            f'where id = {ids}'
                cursor.execute(commando)
                banco.commit()
                self.txt_nomcadfun.setText("")
                self.txt_endcadfun.setText("")
                self.txt_telcadfun.setText("")
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Alterar Cadastro")
                msg.setText("Favor selecione o cliente para ser alterado")
                msg.exec()

    def selecaofun(self):
        ids = self.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
        consulta = f"select nome, telefone, endereco from cadfun where id = {ids}"
        cursor.execute(consulta)
        for (nome, telefone, endereco) in cursor:
            self.txt_nomcadfun.setText(nome)
            self.txt_endcadfun.setText(endereco)
            self.txt_telcadfun.setText(telefone)

    def selecaocli(self):
        ids = self.tableWidget_2.selectionModel().currentIndex().siblingAtColumn(0).data()
        consulta = f"select nome_cl, telcli, endereco_cl from cadastro where id = {ids}"
        cursor.execute(consulta)
        for (nome, telefone, endereco) in cursor:
            self.txt_nomcadcli.setText(nome)
            self.txt_endcadcli.setText(endereco)
            self.txt_telcadcli.setText(telefone)

    def leftMenu(self):
        width = self.left_container.width()

        if width == 0:
            newWidth = 200
        else:
            newWidth = 0

        self.animation = QtCore.QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(1500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def buscar_empresas(self):
        banco.cursor()
        consulta = "select id, nome_cl, telcli, endereco_cl  from cadastro"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(len(linhas))

        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(data)))

    def buscarfun(self):
        banco.cursor()
        consulta = "select id, nome, telefone, endereco from cadfun"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(linhas))

        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))

    def incage(self):
        nomage = self.txt_nomage.text()
        nomagefun = self.txt_agecom.currentText()
        telage = self.txt_telagend.text()
        datage = self.txt_date.text()
        obsage = self.txt_servagend.toPlainText()
        valage = self.txt_valage.text()
        if nomage != "" and nomagefun != "" and datage != "":
            commando = f'INSERT INTO agenda (nomagecli, agefun, agetel, valage, ageobs, dateage) ' \
                       f'VALUES ("{nomage}","{nomagefun}", "{telage}", "{valage}", "{obsage}", "{datage}")'
            cursor.execute(commando)
            banco.commit()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Agendamento de Serviço")
            msg.setText("Agendamento Realizado com sucesso")
            msg.exec()

            self.txt_nomage.setText("")
            self.txt_agecom.setCurrentText("")
            self.txt_telagend.setText("")
            self.txt_servagend.setText("")
            self.txt_valage.setText("")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Agendamento de Serviços")
            msg.setText("Agendamento não realizaso, preencha corretamente os campos")
            msg.exec()

    def tabelaagen(self):
        banco.cursor()
        consulta = "select idagenda, nomagecli, agefun, agetel, dateage, valage, ageobs from agenda"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(len(linhas))
        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(data)))

    def tabelahora(self):
        banco.cursor()
        consulta = "select idagenda, nomagecli, agefun, agetel, dateage, valage, ageobs from agenda"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        self.tableagehora.clearContents()
        self.tableagehora.setRowCount(len(linhas))
        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tableagehora.setItem(row, column, QTableWidgetItem(str(data)))

    def funciona(self):
        consulta = f"SELECT nome from cadfun"
        cursor.execute(consulta)
        self.txt_agecom.clear()
        for (nome) in cursor:
            self.txt_agecom.addItems(nome)

    def pesquisaragendamento(self):
        pesquisa = self.txt_pesqcli.text()
        consulta = f"select idagenda, nomagecli, agefun, agetel, dateage, valage, ageobs from agenda where " \
                   f"nomagecli like '%{pesquisa}%' or nomagecli like '%{pesquisa}%'"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(len(linhas))
        pesquisa = self.txt_pesqcli.text()
        consultavalor = f"SELECT SUM(valage) FROM agenda WHERE " \
                        f"nomagecli like '%{pesquisa}%' or nomagecli like '%{pesquisa}%'"
        cursor.execute(consultavalor)
        total = cursor.fetchone()
        resultado = total[0]
        self.txt_valor.setText(str(resultado))
        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(data)))

    def pesqdata(self):
        datini = self.txt_datini.text()
        datfim = self.txt_datfim.text()
        nomfun = self.txt_pesqvalor.text()
        pesqdat = f"SELECT idagenda, nomagecli, agefun, agetel, dateage, valage, ageobs FROM agenda WHERE " \
                  f"dateage BETWEEN '{datini}' AND '{datfim}' and agefun like '%{nomfun}%'"
        cursor = banco.cursor()
        cursor.execute(pesqdat)
        linhas = cursor.fetchall()
        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(len(linhas))
        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(data)))
                nomfun = self.txt_pesqvalor.text()
                consultavalor = f"SELECT SUM(valage) FROM agenda WHERE " \
                                f"dateage BETWEEN '{datini}' AND '{datfim}' and agefun like '%{nomfun}%'"
                cursor.execute(consultavalor)
                total = cursor.fetchone()
                resultado = total[0]
                self.txt_valor.setText(str(resultado))

    def excluiragenda(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excluir Agendamento")
        msg.setText("Voce tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        ids = self.tableWidget_3.selectionModel().currentIndex().siblingAtColumn(0).data()
        if ids is not None:
            if resp == QMessageBox.Yes:
                banco.cursor()
                commando = f'DELETE FROM agenda WHERE idagenda = {ids}'
                cursor.execute(commando)
                banco.commit()
                self.txt_nomage.setText("")
                self.txt_agecom.setCurrentText("")
                self.txt_telagend.setText("")
                self.txt_servagend.setText("")
                self.txt_valage.setText("")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Cadastro de Agendamento")
            msg.setText("Favor selecione o cliente para ser excluido")
            msg.exec()

    def altefunagenda(self):
        nomage = self.txt_nomage.text()
        nomagefun = self.txt_agecom.currentText()
        telage = self.txt_telagend.text()
        datage = self.txt_date.text()
        obsage = self.txt_servagend.toPlainText()
        valage = self.txt_valage.text()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Alterar Agenda")
        msg.setText("Voce tem certeza que deseja alterar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()
        ids = self.tableWidget_3.selectionModel().currentIndex().siblingAtColumn(0).data()
        if resp == QMessageBox.Yes:
            if nomage != "" and obsage != "" and telage != "" and (ids is not None):
                commando = f'UPDATE agenda SET nomagecli = "{nomage}", ' \
                            f'agefun = "{nomagefun}", ' \
                            f'agetel = "{telage}", ' \
                            f'dateage = "{datage}", ' \
                            f'valage = "{valage}", ' \
                            f'ageobs = "{obsage}" where idagenda = {ids}'
                cursor.execute(commando)
                banco.commit()
                self.txt_nomage.setText("")
                self.txt_agecom.setCurrentText("")
                self.txt_telagend.setText("")
                self.txt_servagend.setText("")
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Alterar Cadastro")
                msg.setText("Favor selecione o cliente para ser alterado")
                msg.exec()

    def buscaragenda(self):
        ids = self.tableWidget_3.selectionModel().currentIndex().siblingAtColumn(0).data()
        consulta = f"select nomagecli, agefun, agetel, dateage, valage, ageobs from agenda where idagenda = {ids}"
        cursor.execute(consulta)
        for (nome, agecom, telage, dateage, valage, ageobs) in cursor:
            self.txt_nomage.setText(nome)
            self.txt_agecom.setCurrentText(agecom)
            self.txt_telagend.setText(telage)
            self.txt_valage.setText(str(valage))
            self.txt_servagend.setText(ageobs)

    def pesquisarvaloresagenda(self):
        funcionario = self.txt_pesqvalor.text()
        consulta = f"select idagenda, nomagecli, agefun, agetel, dateage, valage, ageobs from agenda where " \
                   f"agefun like '%{funcionario}%' or agefun like '%{funcionario}%'"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(len(linhas))
        funcionario = self.txt_pesqvalor.text()
        consultavalor = f"SELECT SUM(valage) FROM agenda WHERE " \
                        f"agefun like '%{funcionario}%' or agefun like '%{funcionario}%'"
        cursor.execute(consultavalor)
        total = cursor.fetchone()
        resultado = total[0]
        self.txt_valor.setText(str(resultado))
        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(data)))

    def inclhora(self):
        nomage = self.txt_nomagehora.text()
        nomagefun = self.txt_agecomhora.currentText()
        telage = self.txt_telagendhora.text()
        datage = self.txt_datehora.text()
        obsage = self.txt_servagendhora.toPlainText()
        valage = self.txt_valagehora.text()
        timehora = self.timemarcar.text()
        if nomage != "" and nomagefun != "" and datage != "":
            commando = f'INSERT INTO agenda (nomagecli, agefun, agetel, valage, ageobs, hora, dateage) VALUES ' \
                        f'("{nomage}","{nomagefun}", "{telage}", "{valage}", "{obsage}","{timehora}", "{datage}")'
            cursor.execute(commando)
            banco.commit()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Agendamento de Horario")
            msg.setText("Agendamento de Horario Realizado com sucesso")
            msg.exec()

            self.txt_nomage.setText("")
            self.txt_agecom.setCurrentText("")
            self.txt_telagend.setText("")
            self.txt_servagend.setText("")
            self.txt_valage.setText("")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Enviar WhatsApp")
            msg.setText("Deseja enviar agendamento via WhatsApp?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            resp = msg.exec()

            if resp == QMessageBox.Yes:
                navegador = webdriver.Chrome()
                navegador.get("https://web.whatsapp.com")

                texto = self.txt_servagendhora.toPlainText()
                telefone = self.txt_telagendhora.text()

                link = f"https://web.whatsapp.com/send?phone={telefone}&text=Funcionária(o): {nomagefun}%0A" \
                       f"Data agendada: {datage} Agendado as: {timehora} %0AOla, {nomage} " \
                       f"Segue serviços agendados: %0A{texto}"

                navegador.get(link)

                while len(navegador.find_elements(By.ID, 'side')) < 1:
                    time.sleep(1)
                time.sleep(2)
                navegador.find_element(By.XPATH,
                                       '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'
                                       ).send_keys(Keys.ENTER)

                time.sleep(5)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Agendamento de Horario")
            msg.setText("Agendamento de horario não realizaso, preencha corretamente os campos")
            msg.exec()

    def exchora(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excluir Horario")
        msg.setText("Voce tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        ids = self.tableagehora.selectionModel().currentIndex().siblingAtColumn(0).data()
        if ids is not None:
            if resp == QMessageBox.Yes:
                banco.cursor()
                commando = f'DELETE FROM agenda WHERE idagenda = {ids}'
                cursor.execute(commando)
                banco.commit()
                self.txt_nomagehora.setText("")
                self.txt_agecomhora.setCurrentText("")
                self.txt_telagendhora.setText("")
                self.txt_servagendhora.setText("")
                self.txt_valagehora.setText("")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Cadastro de Horario")
            msg.setText("Favor selecione o cliente para ser excluido")
            msg.exec()

    def buscarvaloragenda(self):
        consultavalor = f"SELECT SUM(valage) FROM agenda"
        cursor.execute(consultavalor)
        total = cursor.fetchone()
        resultado = total[0]
        self.txt_valorhora.setText(str(resultado))
        self.txt_valor.setText(str(resultado))

    def altehora(self):
        nomage = self.txt_nomagehora.text()
        nomagefun = self.txt_agecomhora.currentText()
        telage = self.txt_telagendhora.text()
        datage = self.txt_datehora.text()
        obsage = self.txt_servagendhora.toPlainText()
        valage = self.txt_valagehora.text()
        timehora = self.timemarcar.text()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Alterar Horario")
        msg.setText("Voce tem certeza que deseja alterar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()
        ids = self.tableagehora.selectionModel().currentIndex().siblingAtColumn(0).data()
        if resp == QMessageBox.Yes:
            if nomage != "" and obsage != "" and telage != "" and (ids is not None):
                commando = f'UPDATE agenda SET nomagecli = "{nomage}", ' \
                            f'agefun = "{nomagefun}", ' \
                            f'agetel = "{telage}", ' \
                            f'dateage = "{datage}", ' \
                            f'valage = "{valage}", ' \
                            f'hora = "{timehora}",' \
                            f'ageobs = "{obsage}" where idagenda = {ids}'
                cursor.execute(commando)
                banco.commit()
                self.txt_nomagehora.setText("")
                self.txt_agecomhora.setCurrentText("")
                self.txt_telagendhora.setText("")
                self.txt_servagendhora.setText("")
                self.txt_valagehora.setText("")
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Alterar Horario")
                msg.setText("Favor selecione o cliente para ser alterado")
                msg.exec()

    def tabelahorario(self):
        banco.cursor()
        consulta = f"select idagenda, nomagecli, agefun, agetel, dateage, hora, valage, ageobs from agenda"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        self.tableagehora.clearContents()
        self.tableagehora.setRowCount(len(linhas))
        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tableagehora.setItem(row, column, QTableWidgetItem(str(data)))

    def buschora(self):
        pesquisa = self.txt_pesclihora.text()
        consulta = f"select idagenda, nomagecli, agefun, agetel, dateage, hora, valage, ageobs from agenda where " \
                   f"nomagecli like '%{pesquisa}%' or nomagecli like '%{pesquisa}%'"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        self.tableagehora.clearContents()
        self.tableagehora.setRowCount(len(linhas))
        funcionario = self.txt_pesclihora.text()
        consultavalor = f"SELECT SUM(valage) FROM agenda WHERE " \
                        f"nomagecli like '%{funcionario}%' or agefun like '%{funcionario}%'"
        cursor.execute(consultavalor)
        total = cursor.fetchone()
        resultado = total[0]
        self.txt_valorhora.setText(str(resultado))
        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tableagehora.setItem(row, column, QTableWidgetItem(str(data)))

    def pesfuncio2(self):
        funcionario = self.txt_pesqvalorhora.text()
        consulta = f"select idagenda, nomagecli, agefun, agetel, dateage, hora, valage, ageobs from agenda where " \
                   f"agefun like '%{funcionario}%' or agefun like '%{funcionario}%'"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        self.tableagehora.clearContents()
        self.tableagehora.setRowCount(len(linhas))
        funcionario = self.txt_pesqvalorhora.text()
        consultavalor = f"SELECT SUM(valage) FROM agenda WHERE " \
                        f"agefun like '%{funcionario}%' or agefun like '%{funcionario}%'"
        cursor.execute(consultavalor)
        total = cursor.fetchone()
        resultado = total[0]
        self.txt_valorhora.setText(str(resultado))
        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tableagehora.setItem(row, column, QTableWidgetItem(str(data)))

    def pesqfunhora(self):
        consulta = f"SELECT nome from cadfun"
        cursor.execute(consulta)
        self.txt_agecomhora.clear()
        for (nome) in cursor:
            self.txt_agecomhora.addItems(nome)

    def tabelaagehora(self):
        ids = self.tableagehora.selectionModel().currentIndex().siblingAtColumn(0).data()
        consulta = f"select nomagecli, agefun, agetel, valage, ageobs from agenda where idagenda" \
                   f" = {ids}"
        cursor.execute(consulta)
        for (nomecliente, nomefuncionario, telefone, valor, obs) in cursor:
            self.txt_nomagehora.setText(nomecliente)
            self.txt_agecomhora.setCurrentText(nomefuncionario)
            self.txt_telagendhora.setText(telefone)
            self.txt_valagehora.setText(str(valor))
            self.txt_servagendhora.setText(obs)


    def pesclihora(self):
        pesquisa = self.txt_pesclihora.text()
        consulta = f"select idagenda, nomagecli, agefun, agetel, dateage, hora, valage, ageobs from agenda where " \
                   f"nomagecli like '%{pesquisa}%' or nomagecli like '%{pesquisa}%'"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        self.tableagehora.clearContents()
        self.tableagehora.setRowCount(len(linhas))
        pesquisa = self.txt_pesclihora.text()
        consultavalor = f"SELECT SUM(valage) FROM agenda WHERE " \
                        f"nomagecli like '%{pesquisa}%' or nomagecli like '%{pesquisa}%'"
        cursor.execute(consultavalor)
        total = cursor.fetchone()
        resultado = total[0]
        self.txt_valorhora.setText(str(resultado))
        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tableagehora.setItem(row, column, QTableWidgetItem(str(data)))

    def funcionahora(self):
        consulta = f"SELECT nome from cadfun"
        cursor.execute(consulta)
        self.txt_agecomhora.clear()
        for (nome) in cursor:
            self.txt_agecomhora.addItems(nome)

    def tabestoque(self):
        consulta = "select IDPRODUTOS, PRODUTOS, VALOR, DATA, QUANTIDADE from PRODUTOS"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        self.tabelaestoque.clearContents()
        self.tabelaestoque.setRowCount(len(linhas))
        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tabelaestoque.setItem(row, column, QTableWidgetItem(str(data)))

    def incluestoque(self):
        produto = self.txt_produto.text()
        valor = self.txt_valproesto.text()
        data = self.txt_datproesto.text()
        quantidade = self.txt_qtdesto.text()
        inseprodutos = f'INSERT INTO produtos (PRODUTOS, VALOR, DATA, QUANTIDADE) VALUES ' \
                       f'("{produto}","{valor}","{data}","{quantidade}")'
        cursor.execute(inseprodutos)
        banco.commit()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Estoque de Produtos")
        msg.setText("Produto Cadastrado com sucesso")
        msg.exec()

        self.txt_produto.setText("")
        self.txt_valproesto.setText("")
        self.txt_qtdesto.setText("")

    def valprodutostotal(self):
        valtotalpro = f'select sum(valor) from produtos'
        cursor.execute(valtotalpro)
        total = cursor.fetchone()
        self.txt_valtotoestoq.clear()
        resultado = total[0]
        self.txt_valtotoestoq.setText(str(resultado))

    def buscarprodutostabela(self):
        ids = self.tabelaestoque.selectionModel().currentIndex().siblingAtColumn(0).data()
        consulta = f"select PRODUTOS, VALOR, DATA, QUANTIDADE from produtos where IDPRODUTOS = {ids}"
        cursor.execute(consulta)
        for (produtos, valor, data, quantidade) in cursor:
            self.txt_produto.setText(produtos)
            self.txt_agecomhora.setCurrentText(data)
            self.txt_valproesto.setText(str(valor))
            self.txt_qtdesto.setText(str(quantidade))

    def alprodutos(self):
        produto = self.txt_produto.text()
        valor = self.txt_valproesto.text()
        data = self.txt_datproesto.text()
        quantidade = self.txt_qtdesto.text()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Alterar Produto")
        msg.setText("Voce tem certeza que deseja alterar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()
        ids = self.tabelaestoque.selectionModel().currentIndex().siblingAtColumn(0).data()
        if resp == QMessageBox.Yes:
            if produto != "" and valor != "" and quantidade != "" and (ids is not None):
                commando = f'UPDATE PRODUTOS SET produtos = "{produto}", valor = "{valor}",data =' \
                            f' "{data}", quantidade = {quantidade} where idprodutos = {ids}'
                cursor.execute(commando)
                banco.commit()
                self.txt_produto.setText("")
                self.txt_valproesto.setText("")
                self.txt_qtdesto.setText("")
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Alterar Produtos")
                msg.setText("Favor selecione o produto para ser alterado")
                msg.exec()

    def excluirestoque(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excluir Produto")
        msg.setText("Voce tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()
        ids = self.tabelaestoque.selectionModel().currentIndex().siblingAtColumn(0).data()
        if ids is not None:
            if resp == QMessageBox.Yes:
                banco.cursor()
                commando = f'DELETE FROM PRODUTOS WHERE IDPRODUTOS = {ids}'
                cursor.execute(commando)
                banco.commit()
                self.txt_produto.setText("")
                self.txt_valproesto.setText("")
                self.txt_qtdesto.setText("")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Cadastro de Produtos")
            msg.setText("Favor selecione o produto para ser excluido")
            msg.exec()

    def pescpro(self):
        pesquisa = self.txt_pesqesto.text()
        consulta = f"select IDPRODUTOS, PRODUTOS, VALOR, DATA, QUANTIDADE from produtos where " \
                   f"produtos like '%{pesquisa}%' or produtos like '%{pesquisa}%'"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        if not linhas:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Produtos")
            msg.setText("Produto não encontrado!")
            msg.exec()
        else:
            self.tabelaestoque.clearContents()
            self.tabelaestoque.setRowCount(len(linhas))
            pesquisa = self.txt_pesqesto.text()
            consultavalor = f"SELECT SUM(valor) FROM produtos WHERE produtos like" \
                            f" '%{pesquisa}%' or produtos like '%{pesquisa}%'"
            cursor.execute(consultavalor)
            total = cursor.fetchone()
            resultado = total[0]
            self.txt_valtotoestoq.setText(str(resultado))
            for row, text in enumerate(linhas):
                for column, data in enumerate(text):
                    self.tabelaestoque.setItem(row, column, QTableWidgetItem(str(data)))

    def tabepromo(self):
        banco.cursor()
        consulta = "select id, nome_cl, telcli, endereco_cl  from cadastro"
        cursor = banco.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        self.tabelapromoes.clearContents()
        self.tabelapromoes.setRowCount(len(linhas))
        for row, text in enumerate(linhas):
            for column, data in enumerate(text):
                self.tabelapromoes.setItem(row, column, QTableWidgetItem(str(data)))

    def enviarpromocao(self):
        banco.cursor()
        telcli = "select telcli, nome_cl from cadastro"
        cursor = banco.cursor()
        cursor.execute(telcli)
        menssagem = self.txt_textopromo.toPlainText()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Enviar WhatsApp")
        msg.setText("Deseja enviar agendamento via WhatsApp?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            navegador = webdriver.Chrome()
            navegador.get("https://web.whatsapp.com")
            for (telefone, cliente) in cursor:
                link = f"https://web.whatsapp.com/send?phone={telefone}&text=%0AOla, {cliente}, " \
                    f" Estamos com novidades: %0A{menssagem}"
                navegador.get(link)
                while len(navegador.find_elements(By.ID, 'side')) < 1:
                    time.sleep(1)
                time.sleep(2)
                navegador.find_element(By.XPATH,
                                       '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'
                                       ).send_keys(Keys.ENTER)

                time.sleep(5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
