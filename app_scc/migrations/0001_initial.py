# Generated by Django 4.1.4 on 2022-12-26 14:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatos',
            fields=[
                ('cpf', models.CharField(help_text='Somente números*', max_length=11, primary_key=True, serialize=False, verbose_name='CPF do(a) Candidato(a)')),
                ('nome', models.CharField(help_text='Completo e em caixa alta, sem abreviações*', max_length=100, null=True, verbose_name='Nome do(a) Candidato(a)')),
                ('telefone', models.CharField(help_text='ex:(ddd)940028922', max_length=13, null=True, verbose_name='Telefone')),
                ('municipio', models.CharField(choices=[('Alvarães', 'Alvarães'), ('Amaturá', 'Amaturá'), ('Anamã', 'Anamã'), ('Anori', 'Anori'), ('Apuí', 'Apuí'), ('Atalaia do Norte', 'Atalaia do Norte'), ('Autazes', 'Autazes'), ('Barcelos', 'Barcelos'), ('Barreirinha', 'Barreirinha'), ('Benjamin Constant', 'Benjamin Constant'), ('Beruri', 'Beruri'), ('Boa Vista do Ramos', 'Boa Vista do Ramos'), ('Boca do Acre', 'Boca do Acre'), ('Borba', 'Borba'), ('Caapiranga', 'Caapiranga'), ('Canutama', 'Canutama'), ('Carauari', 'Carauari'), ('Careiro', 'Careiro'), ('Careiro da Várzea', 'Careiro da Várzea'), ('Coari', 'Coari'), ('Codajás', 'Codajás'), ('Eirunepé', 'Eirunepé'), ('Envira', 'Envira'), ('Fonte Boa', 'Fonte Boa'), ('Guajará', 'Guajará'), ('Humaitá', 'Humaitá'), ('Ipixuna', 'Ipixuna'), ('Iranduba', 'Iranduba'), ('Itacoatiara', 'Itacoatiara'), ('Itamarati', 'Itamarati'), ('Itapiranga', 'Itapiranga'), ('Japurá', 'Japurá'), ('Juruá', 'Juruá'), ('Jutaí', 'Jutaí'), ('Lábrea', 'Lábrea'), ('Manacapuru', 'Manacapuru'), ('Manaquiri', 'Manaquiri'), ('Manaus', 'Manaus'), ('Manicoré', 'Manicoré'), ('Maraã', 'Maraã'), ('Maués', 'Maués'), ('Nhamundá', 'Nhamundá'), ('Nova Olinda do Norte', 'Nova Olinda do Norte'), ('Novo Airão', 'Novo Airão'), ('Novo Aripuanã', 'Novo Aripuanã'), ('Parintins', 'Parintins'), ('Pauini', 'Pauini'), ('Presidente Figueiredo', 'Presidente Figueiredo'), ('Rio Preto da Eva', 'Rio Preto da Eva'), ('Santa Isabel do Rio Negro', 'Santa Isabel do Rio Negro'), ('Santo Antônio do Içá', 'Santo Antônio do Içá'), ('São Gabriel da Cachoeira', 'São Gabriel da Cachoeira'), ('São Paulo de Olivença', 'São Paulo de Olivença'), ('São Sebastião do Uatumã', 'São Sebastião do Uatumã'), ('Silves', 'Silves'), ('Tabatinga', 'Tabatinga'), ('Tapauá', 'Tapauá'), ('Tefé', 'Tefé'), ('Tonantins', 'Tonantins'), ('Uarini', 'Uarini'), ('Urucará', 'Urucará'), ('Urucurituba', 'Urucurituba')], default='Campo não alterado', max_length=30, null=True, verbose_name='Município')),
                ('categoria_cnh', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1, null=True, verbose_name='Categoria CNH Solici.')),
                ('servico', models.CharField(choices=[('1A.CNH', '1A.CNH'), ('TROCA/ADIC', 'TROCA/ADIC')], max_length=10, null=True, verbose_name='Tipo de serviço solicitado')),
                ('exame_medico', models.CharField(blank=True, choices=[('Apto', 'Apto'), ('Inapto', 'Inapto'), ('Apto com restrição', 'Apto com restrição'), ('Reavaliação', 'Reavaliação')], max_length=18, verbose_name='Situação do exame médico')),
                ('formacao_teorica', models.CharField(blank=True, choices=[('Não realizada', 'Não realizada'), ('Realizada', 'Realizada'), ('Em andamento', 'Em andamento')], max_length=13, verbose_name='Status da formação teórica')),
                ('exame_teorico', models.CharField(blank=True, choices=[('Apto', 'Apto'), ('Inapto', 'Inapto'), ('Faltoso', 'Faltoso')], max_length=7, verbose_name='Situação exame teórico')),
                ('curso_direcao', models.CharField(blank=True, choices=[('Realizado', 'Realizado'), ('Em andamento', 'Em andamento'), ('Não realizado', 'Não realizado')], max_length=13, verbose_name='Status do curso de direção')),
                ('exame_direcao', models.CharField(blank=True, choices=[('Apto', 'Apto'), ('Inapto', 'Inapto'), ('Faltoso', 'Faltoso')], max_length=7, verbose_name='Situação do exame de direção')),
                ('emissao_cnh', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='CNH emitida?')),
                ('justificativas_auditoria_jm', models.TextField(default='Correção não realizada.', help_text='obs*: Limpe a caixa de texto acima e justifique o motivo da correção!', max_length=240, verbose_name='Justificativa para fins de auditoria')),
                ('justificativas_auditoria_cedv', models.TextField(default='Correção não realizada.', help_text='obs*: Limpe a caixa de texto acima e justifique o motivo da correção!', max_length=240, verbose_name='Justificativa para fins de auditoria')),
                ('justificativas_auditoria_crt', models.TextField(default='Correção não realizada.', help_text='obs*: Limpe a caixa de texto acima e justifique o motivo da correção!', max_length=240, verbose_name='Justificativa para fins de auditoria')),
                ('justificativas_auditoria_cnh', models.TextField(default='Correção não realizada.', help_text='obs*: Limpe a caixa de texto acima e justifique o motivo da correção!', max_length=240, verbose_name='Justificativa para fins de auditoria')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Data de criação do registro')),
            ],
            options={
                'verbose_name': 'Candidato',
                'verbose_name_plural': 'Candidatos',
                'db_table': 'Candidatos',
                'ordering': ('data_criacao',),
                'permissions': [('pode_manipular_cnh', 'pode manipular cnh'), ('pode_manipular_jm', 'pode manipular jm'), ('pode_manipular_crt', 'pode manipular crt'), ('pode_manipular_cedv', 'pode manipular cedv')],
            },
        ),
    ]
